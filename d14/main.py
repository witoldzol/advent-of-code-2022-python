import sys
from typing import List, Tuple

def main(filename):
    coords = get_coords(filename)
    cave = draw_cave(coords)
    x_labels = [f"{i}" for i in range(len(cave))]
    print('[x]', end='')
    print(x_labels)
    for i,row in enumerate(cave):
        print(f"[{i}]", end='')
        print(row)


def get_coords(filename: str) ->List[List[List[int]]]:
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
    print(result)
    return result

def get_min_max_x_y(coords: List[List[List[int]]]) -> Tuple[int, int, int, int]:
    min_x = sys.maxsize
    # min_x = 0
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
    # max_x, max_y = swap(max_x, max_y)
    print(f"[LOG] min_x = {min_x}, min_y = {min_y}, max_x = {max_x}, max_y = {max_y}")
    return min_x, max_x, min_y, max_y

def swap(x,y):
    temp = x
    x = y
    y = temp
    return x,y

# todo - I think we  have to swap x & y coords in the array as well
def draw_cave(coords: List[List[List[int]]]) -> List[List[int]]:
    # draw empty cave
    min_x, max_x, min_y, max_y = get_min_max_x_y(coords)
    cave = [[] for _ in range(min_x,max_x+1)]
    for x in cave:
        for _ in range(min_y,max_y+1):
            x.append('.')
    # draw rocks
    for c in coords:
        for i in range(len(c)-1):
            start_x,start_y = c[i]
            end_x,end_y = c[i+1]
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
            # swap x & y
            start_x, start_y = swap(start_x, start_y)
            end_x, end_y = swap(end_x, end_y)
            if start_x - end_x == 0:
                for i in range(start_y, end_y+1):
                    cave[start_x][i] = '#'
            else:
                pass
                for i in range(start_x, end_x+1):
                    cave[i][start_y] = '#'
    # done
    return cave
if __name__ == "__main__":
    main('sample_input')
    # main('input')
