import sys
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
    min_x = sys.maxsize
    min_y = 0
    max_x = -1
    max_y = -1
    for c in coords:
        x, y = c
        if x < min_x:
            min_x = x
        elif x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        elif y > max_y:
            max_y = y
    for  # todo finish drawing a cave 2d matrix
    return [[]]

if __name__ == "__main__":
    main('sample_input')
