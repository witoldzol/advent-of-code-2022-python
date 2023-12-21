from typing import List

class Valve():
    def __init__(self, name: str, rate:int, adjecent: List[str]) -> None:
        self.adjecent = adjecent
        self.name = name
        self.rate = rate
    def __repr__(self) -> str:
        return f'{self.name=}, {self.rate=}, {self.adjecent=}'

def parse_input(filename: str):
    valves = []
    data = open(filename, "r").read().strip()
    lines = data.split("\n")
    for l in lines:
        chunks = l.split(' ')
        name = chunks[1]
        _,rate = chunks[4].split('=')
        rate = int(rate[:-1])
        adjecent = chunks[9:]
        valves.append(Valve(name,rate,adjecent))
    return valves


def main(input):
    valves = parse_input(input)
    for v in valves:
        print(v)


if __name__ == "__main__":
    input = "sample_input"
    input = "input"
    input = "small_input"
    main(input)
