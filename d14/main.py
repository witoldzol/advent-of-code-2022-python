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
            temp = []
            for c in coords:
                out = [int(x) for x in c.split(',')]
                temp.append(out)
            result.append(temp)
            temp = []
    print("========================================")
    print(result)
    print("========================================")
    return result

def get_min_max_x_y(coords: List[List[List[int]]]) -> Tuple[int, int, int, int]:
    min_x = sys.maxsize
    min_y = 0
    max_x = -1
    max_y = -1
    for c in coords:
        for x,y in c:
            if x < min_x:
                min_x = x
            elif x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            elif y > max_y:
                max_y = y
    return min_x, max_x, min_y, max_y



def draw_cave(coords: List[List[List[int]]]) -> List[List[str]]:
    # draw empty cave
    min_x, max_x, min_y, max_y = get_min_max_x_y(coords)
    cave = [[] for _ in range(min_x,max_x)]
    for x in cave:
        for _ in range(min_y,max_y):
            x.append('.')
    # draw rocks
    # [[498,4 , 498,6 , 496,6],[....],[....]]
    for c in coords:
        print(c)




    # done
    return cave
if __name__ == "__main__":
    main('sample_input')
