from typing import List, Dict


class Valve:
    def __init__(self, name: str, rate: int, adjecent: List[str]) -> None:
        self.adjecent = adjecent
        self.name = name
        self.rate = rate

    def __repr__(self) -> str:
        return f"Valve(name={self.name}, rate={self.rate}, adjecent={self.adjecent})"


def parse_input(filename: str) -> Dict[str,Valve]:
    valves = {}
    data = open(filename, "r").read().strip()
    lines = data.split("\n")
    for l in lines:
        chunks = l.split(" ")
        name = chunks[1]
        _, rate = chunks[4].split("=")
        rate = int(rate[:-1])
        adjecent = chunks[9:]
        adjecent = ' '.join(adjecent)
        adjecent = adjecent.split(',')
        adjecent = [x.strip() for x in adjecent]
        valves[name] = Valve(name, rate, adjecent)
    return valves

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

def print_possible_paths(root: Valve, valves) -> None:
    for adjecent in root.adjecent:
        print(adjecent)


def main(input):
    valves = parse_input(input)
    for turn in range(1,31):
        print_possible_paths(valves['AA'], valves)



if __name__ == "__main__":
    input = "sample_input"
    input = "input"
    input = "small_input"
    main(input)
