import sys
from typing import List, Tuple

def main(filename):
    coords = get_coords(filename)
    cave = draw_cave(coords)
    for row in cave:
        print(row)

def get_coords(filename: str) -> List[List[int]]:
    with open(filename, 'r') as input:
        result = []
        for line in input:
            coords = line.strip().split('->')
            for c in coords:
                out = [int(x) for x in c.split(',')]
                result.append(out)
    return result

def get_min_max_x_y(coords: List[List[int]]) -> Tuple[int, int, int, int]:
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
    return min_x, max_x, min_y, max_y

def draw_cave(coords: List[List[int]]) -> List[List[str]]:
    min_x, max_x, min_y, max_y = get_min_max_x_y(coords)
    # populate with dots
    cave = [[] for _ in range(min_x,max_x)]
    for x in cave:
        for _ in range(min_y,max_y):
            x.append('.')
    for x,y in coords:
        x = x - min_x
        y = y - min_y
        print('x ', x)
        print(y)
        cave[x][y] = '#'
    return cave

if __name__ == "__main__":
    main('sample_input')
