from typing import List, Dict, Set, Tuple
from collections import OrderedDict
import pudb

class Valve:
    def __init__(self, name: str, rate: int, adjacent: List["Valve"] = None) -> None:
        self.adjacent = adjacent
        self.name = name
        self.rate = rate
    def __repr__(self) -> str:
        return f"Valve(name={self.name}, rate={self.rate}, adjacent={[v.name for v in self.adjacent]})"


def calculate_returns(
    start: Valve, map: Dict[str, Valve], max_turns: int
    ) -> Tuple[Dict[str, int], int]:
    max_returns_map = OrderedDict()
    max_flow = 0
    max_value_valve = ""
    jump = 0
    turn = max_turns
    for _ in range(len(map)):
        print(f"Turns left == {turn}, current valve is {start.name}")
        for valve in map.values():
            if valve.name == start.name or valve.name in max_returns_map or valve.rate == 0:
                continue
            path_to_valve = BFS(start, valve.name)
            print(f"path to valve {valve.name} takes {path_to_valve[1]} turns + 1 turn to turn on the valve")
            if not path_to_valve:
                raise Exception(f"Unable to find path to valve {valve.name}")
            _, turns_to_get_to_valve = path_to_valve
            turns_to_get_to_valve += 1  # one extra turn to activate the valve
            remaining_turns = turn - turns_to_get_to_valve
            print(f"remaining turns for node {valve.name} is {remaining_turns}")
            potential_flow = valve.rate * remaining_turns
            print(f"potential flow for node {valve.name} is {potential_flow}")
            if potential_flow > max_flow:
                max_flow = potential_flow
                max_value_valve = valve.name
                jump = turns_to_get_to_valve
        # exit early if more turns than valves
        turn -= jump
        if not max_value_valve:
            print("===================")
            print(f"{max_returns_map=}")
            print("===================")
            return max_returns_map
        print(f"==> MAX flow is {max_flow} at node {max_value_valve} and it takes {jump} turns to get there from node {start.name}")
        max_returns_map[max_value_valve] = max_flow
        start = map[max_value_valve]
        max_flow = 0
        max_value_valve = ""
    print("===================")
    print(f"{max_returns_map=}")
    print("===================")
    return max_returns_map, turn


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


def BFS(
    root: Valve,
    target: str,
    map: Dict[str, bool] | None = None,
    path: str = "",
    jumps: int = -1,
) -> Tuple[str, int] | None:
    if not map:
        map = {}
    if not root:
        return "", jumps
    path += root.name
    map[root.name] = True
    jumps += 1
    if root.name == target:
        return path, jumps
    result = ""
    for v in root.adjacent:
        if not v.name in map:
            result = BFS(v, target, map, path, jumps)
            if result:
                return result


def calculate_returns2(
    start: Valve,
    map: Dict[str, Valve],
    max_turns: int,
    max_returns_map: OrderedDict[str,int]
) -> OrderedDict[str, int]:
    max_flow = 0
    max_value_valve = ""
    jump = 0
    turn = max_turns
    print(f"Turns left == {turn}, current valve is {start.name}")
    for valve in map.values():
        if valve.name == start.name or valve.name in max_returns_map or valve.rate == 0:
            continue
        path_to_valve = BFS(start, valve.name)
        print(f"path to valve {valve.name} takes {path_to_valve[1]} turns + 1 turn to turn on the valve")
        if not path_to_valve:
            raise Exception(f"Unable to find path to valve {valve.name}")
        _, turns_to_get_to_valve = path_to_valve
        turns_to_get_to_valve += 1  # one extra turn to activate the valve
        remaining_turns = turn - turns_to_get_to_valve
        print(f"remaining turns for node {valve.name} is {remaining_turns}")
        potential_flow = valve.rate * remaining_turns
        print(f"potential flow for node {valve.name} is {potential_flow}")
        if potential_flow > max_flow:
            max_flow = potential_flow
            max_value_valve = valve.name
            jump = turns_to_get_to_valve
    # exit early if more turns than valves
    turn -= jump
    if not max_value_valve:
        print("===================")
        print(f"{max_returns_map=}")
        print("===================")
        return max_returns_map
    print(f"==> MAX flow is {max_flow} at node {max_value_valve} and it takes {jump} turns to get there from node {start.name}")
    max_returns_map[max_value_valve] = max_flow
    print("===================")
    print(f"{max_returns_map=}")
    print("===================")
    return max_returns_map, turn


def calculate_returns3(
    start: Valve,
    map: Dict[str, Valve],
    max_turns: int,
    ) -> List[Tuple[str,int]]:
    results = []
    for valve in map.values():
        if valve.name == start.name:
            continue
        path_to_valve = BFS(start, valve.name)
        print(f"path to valve {valve.name} takes {path_to_valve[1]} turns + 1 turn to turn on the valve")
        if not path_to_valve:
            raise Exception(f"Unable to find path to valve {valve.name}")
        _, turns_to_get_to_valve = path_to_valve
        turns_to_get_to_valve += 1  # one extra turn to activate the valve
        remaining_turns = max_turns - turns_to_get_to_valve
        print(f"remaining turns for node {valve.name} is {remaining_turns}")
        potential_flow = valve.rate * remaining_turns
        print(f"potential flow for node {valve.name} is {potential_flow}")
        valve_flow_pair = (valve.name, potential_flow)
        results.append(valve_flow_pair)
    return results


def main(input):
    root, valves = build_valve_graph(input)
    sum = 0
    returns_map = calculate_returns(root, valves, 30)
    for k,v in returns_map.items():
        sum += v
    print(f"max is = {sum}")



if __name__ == "__main__":
    input = "sample_input"
    # input = "input"
    # input = "small_input"
    main(input)
