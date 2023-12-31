from typing import List, Dict, Set, Tuple
import pudb


class Valve:
    def __init__(self, name: str, rate: int, adjacent: List["Valve"] = None) -> None:
        self.adjacent = adjacent
        self.name = name
        self.rate = rate
        self.visited = False

    def __repr__(self) -> str:
        return f"Valve(name={self.name}, rate={self.rate}, adjacent={[v.name for v in self.adjacent]})"


def build_valve_graph(filename: str) -> Tuple[Valve, Dict[str, Valve]]:
    valves = {}
    data = open(filename, "r").read().strip()
    lines = data.split("\n")
    adjacent_dict = {}
    for l in lines:
        chunks = l.split(" ")
        name = chunks[1]
        _, rate = chunks[4].split("=")
        rate = int(rate[:-1])
        adjacent = chunks[9:]
        adjacent = " ".join(adjacent)
        adjacent = adjacent.split(",")
        adjacent = [x.strip() for x in adjacent]
        valves[name] = Valve(name, rate)
        adjacent_dict[name] = adjacent
    for valve in valves.values():
        valve.adjacent = []
        adjacent_valves = adjacent_dict[valve.name]
        for name in adjacent_valves:
            valve.adjacent.append(valves[name])
    return valves["AA"], valves


def BFS(root: Valve, target: str, map: Dict[str, bool], path: str = "", jumps: int = -1 ) -> Tuple[str, int]:
    print(f"map has been passed in {map}")
    if not root:
        return "", jumps
    path += root.name
    root.visited = True
    map[root.name] = True
    jumps += 1
    if root.name == target:
        return path, jumps
    result = ""
    for v in root.adjacent:
        if v.visited != map[v.name]:
            print(f"there is a mismatch between {v.name} = {v.visited} and the map {v.name} = {map[v.name]}")
        if not v.visited:
            # print(f"visiting node {root.name}, checking adjecent node {v.name}, in map it is marked as {map[v.name]}")
            result = BFS(v, target, map, path, jumps)
            if result:
                return result
    return '', -1

def calculate_returns(start: Valve, map: Dict[str, Valve], current_turn: int) -> Dict[str, int]:
    # pu.db
    returns_map = {}
    for valve in map.values():
        print(f"{valve=}")
        if valve.name == start.name:
            continue
        result = BFS(start, valve.name)
        if not result:
            raise Exception(f'Unable to find path to valve {valve.name}')
        _, turns_to_get_to_valve = result
        turns_to_get_to_valve += 1 # one extra turn to activate the valve
        remaining_turns = current_turn - turns_to_get_to_valve
        potential_flow = valve.rate * remaining_turns
        returns_map[valve.name] = potential_flow
    return returns_map


def main(input):
    root, valves = build_valve_graph(input)
    print(root)
    path = BFS(root, "JJ")
    print(f"{path=}")


if __name__ == "__main__":
    input = "sample_input"
    # input = "input"
    # input = "small_input"
    main(input)
