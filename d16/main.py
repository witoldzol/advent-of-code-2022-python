from typing import List, Dict, Set


class Valve:
    def __init__(self, name: str, rate: int, adjecent: List[str]=None) -> None:
        self.adjecent = adjecent
        self.name = name
        self.rate = rate

    def __repr__(self) -> str:
        return f"Valve(name={self.name}, rate={self.rate}, adjecent={self.adjecent})"


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


# def DFS(root: Valve, valves: Dict[str,Valve], count: int):
#     count += 1
#     if count >= 30:
#         return None
#     if not root.adjecent:
#         return None
#     for valve in root.adjecent:
#         print(f'{valve=}')
#         print(f'going from {root=} to {valve=}')
#         DFS(valves[valve], valves, count)


def main(input):
    root = build_valve_graph(input)
    print(root)


if __name__ == "__main__":
    input = "sample_input"
    input = "input"
    input = "small_input"
    main(input)
