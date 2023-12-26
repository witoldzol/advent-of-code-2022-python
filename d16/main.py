from typing import List, Dict, Set


class Valve:
    def __init__(self, name: str, rate: int, adjecent: List["Valve"] = None) -> None:
        self.adjecent = adjecent
        self.name = name
        self.rate = rate
        self.visited = False

    def __repr__(self) -> str:
        return f"Valve(name={self.name}, rate={self.rate}, adjecent={[v.name for v in self.adjecent]})"


def build_valve_graph(filename: str) -> Valve:
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
    return valves['AA']


def DFS(root: Valve, turn: int) -> None:
    root.visited = True
    print(f'This is {turn=}, visited {root.name}')
    turn += 1
    for valve in root.adjecent:
        if not valve.visited:
            DFS(valve, turn)


def main(input):
    root = build_valve_graph(input)
    # print(root)
    DFS(root, 0)


if __name__ == "__main__":
    input = "sample_input"
    input = "input"
    input = "small_input"
    main(input)
