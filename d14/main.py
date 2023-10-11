from typing import List

def main(filename):
    coords = get_coords(filename)
    cave = draw_cave(coords)
    print(cave)

def get_coords(filename: str) -> List[List[int]]:
    with open(filename, 'r') as input:
        result = []
        for line in input:
            coords = line.strip().split('->')
            for c in coords:
                out = [int(x) for x in c.split(',')]
                result.append(out)
    return result

def draw_cave(coords: List[List[int]]) -> List[List[str]]:
    return [[]]

if __name__ == "__main__":
    main('sample_input')
