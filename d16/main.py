from typing import List, Dict, Set, Tuple


class Valve:
    def __init__(self, name: str, rate: int, adjacent: List["Valve"] = None) -> None:
        self.adjecent = adjacent
        self.name = name
        self.rate = rate
        self.visited = False

    def __repr__(self) -> str:
        return f"Valve(name={self.name}, rate={self.rate}, adjecent={[v.name for v in self.adjecent]})"


def build_valve_graph(filename: str) -> Tuple[Valve, Dict[str,Valve]]:
    valves = {}
    data = open(filename, "r").read().strip()
    lines = data.split("\n")
    adjecent_dict = {}
    for l in lines:
        chunks = l.split(" ")
        name = chunks[1]
        _, rate = chunks[4].split("=")
        rate = int(rate[:-1])
        adjecent = chunks[9:]
        adjecent = ' '.join(adjecent)
        adjecent = adjecent.split(',')
        adjecent = [x.strip() for x in adjecent]
        valves[name] = Valve(name, rate)
        adjecent_dict[name] = adjecent
    for valve in valves.values():
        valve.adjecent = []
        adjecent_valves = adjecent_dict[valve.name]
        for name in adjecent_valves:
            valve.adjecent.append(valves[name])
    return valves['AA'], valves

def find_valve(root: Valve, turn: int, target: str, path: List[str] = None) -> List[str] | None:
    if not path:
        path = []
    new_path = path.copy()
    new_path.append(root.name)
    root.visited = True
    if root.name == target:
        return new_path
    path.append(root.name)
    print(f'This is {turn=}, visited {root.name}')
    turn += 1
    result = None
    for valve in root.adjecent:
        if not valve.visited:
            result =  find_valve(valve, turn, target, new_path)
    if result:
        return result


def DFS(root: Valve, target: str, path: str = "") -> str:
    if not root:
        return ""
    path += root.name
    root.visited = True
    if root.name == target:
        return path
    result = ""
    for v in root.adjecent:
        if not v.visited:
            result =  DFS(v, target, path)
    if result:
        return result


def main(input):
    root, valves = build_valve_graph(input)
    # print(root)
    # DFS(root, 0)
    # path = find_valve(root,0,'DD')
    path = DFS(root,'DD')
    print(f'{path=}')


if __name__ == "__main__":
    input = "sample_input"
    # input = "input"
    # input = "small_input"
    main(input)

# todo
# build graph - done
# get a 'map' of nodes and connections - done
# traverse map from one node to another using BFS - done
# run 30 turns, going from highest expected pay to another - 
