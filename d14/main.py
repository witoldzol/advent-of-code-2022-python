import sys
from typing import List, Tuple


def main(filename):
    coords = get_coords(filename)
    cave, entry_coordinates = draw_cave(coords) #entry coords are not swapped!, we have real x,y
    move_sand(cave, entry_coordinates)
    for row in cave:
        print(row)

def move_sand(cave:List[List[str]],sand_coords: Tuple[int,int]) -> None:
    x,y = sand_coords
    one_below = cave[x+1][y] # cave axis are swapped, x=>y, y=>x, so we move down the x (aka y) axis
    if one_below == '.':
        print('empty space, sand is moving down')
        cave[x+1][y] = '*'



def get_coords(filename: str) ->List[List[List[int]]]:
    with open(filename, 'r') as input:
        result = []
        for line in input:
            temp = []
            coords = line.strip().split('->')
            for c in coords:
                out = [int(x) for x in c.split(',')]
                temp.append(out)
            result.append(temp)
    print(result)
    return result

def draw_cave(coords: List[List[List[int]]]) -> List[List[str]]:
    # draw empty cave
    # swapped x and y
    min_y, max_y, min_x, max_x = get_min_max_x_y(coords)
    # we already swapped x for y=> we still need to use actual x value here
    sand_entry_point = 500 - min_y
    cave = [[] for _ in range(min_x,max_x+1)]
    for x in cave:
        for _ in range(min_y,max_y+1):
            x.append('.')
    # draw rocks
    for c in coords:
        for i in range(len(c)-1):
            # swapped x and y
            start_y,start_x = c[i]
            end_y, end_x = c[i+1]
            print(f'drawing {start_x},{start_y} ->{end_x},{end_y}')
            # adjust to 0 index
            start_x = start_x-min_x
            start_y = start_y-min_y
            end_x = end_x-min_x
            end_y = end_y-min_y
            print('start x ', start_x, 'end x ', end_x)
            print('start y ', start_y, 'end y ', end_y)
            if start_x > end_x:
                start_x,end_x = swap(start_x,end_x)
            if start_y > end_y:
                start_y,end_y = swap(start_y,end_y)
            if start_x - end_x == 0:
                for i in range(start_y, end_y+1):
                    cave[start_x][i] = '#'
            else:
                pass
                for i in range(start_x, end_x+1):
                    cave[i][start_y] = '#'
    # sand entry point - axis are swapped!, normally it would be cave[500][0]
    cave[0][sand_entry_point] = '+'
    return cave, (0,sand_entry_point)

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
    print(f"[LOG] min_x = {min_x}, min_y = {min_y}, max_x = {max_x}, max_y = {max_y}")
    return min_x, max_x, min_y, max_y

def swap(x,y):
    temp = x
    x = y
    y = temp
    return x,y

if __name__ == "__main__":
    main('sample_input')
    # main('input')
