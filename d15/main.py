import cProfile
from typing import Tuple, List, Dict
import re
import logging as log
import argparse

MAX_REGION = 4_000_000


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-log")
    log_level = parser.parse_args().log
    log.basicConfig(level=log_level)


def parse_line(line: str) -> Tuple[int, int, int, int]:
    pattern = r".*x=(.*),.*y=(.*):.*x=(.*),.*y=(.*)$"
    m = re.search(pattern, line)
    if m:
        sx, sy, bx, by = m.groups()
        sx, sy, bx, by = int(sx), int(sy), int(bx), int(by)
        log.debug(f"sx = {sx}, sy={sy}, bx={bx}, by={by}")
        return sx, sy, bx, by
    else:
        print("no match")
    raise Exception(f"Failed to parse the input: \n{line}")


def parse_data(filename) -> List[Tuple[int, int, int, int]]:
    f = open(filename, "r")
    data = f.read().strip()
    lines = data.split("\n")
    coords = []
    for l in lines:
        c = parse_line(l)
        coords.append(c)
    return coords


def generate_manhatan_lengths(
    coords: Tuple[int, int, int, int], row: int
) -> List[Tuple[int, int]]:
    m_lenghts = set()
    sx, sy, bx, by = coords
    dx = abs(sx - bx)
    log.debug(f"Delta x = {dx}")
    dy = abs(sy - by)
    log.debug(f"Delta y = {dy}")
    dd = dx + dy
    if not dd:
        return []
    log.debug(f"Max Delta = {dd}")
    # check if we are in range of required row
    if row > sy:
        if sy + dd < row:  # we cant reach row 'above' sy
            return []
    else:
        if sy - dd > row:
            return []
    # calculate distance to required row
    if sy <= row:
        i = row - sy
    else:
        i = sy - row
    # print(f"{i=}")
    # x ,y
    edge = (sx + dd - i, sy + i)
    if edge[1] == row:
        m_lenghts.add(edge)
        log.debug(f"+x,+y quadrant edge: {edge}")
    # -x, y
    edge = (sx - dd + i, sy + i)
    if edge[1] == row:
        m_lenghts.add(edge)
        log.debug(f"+x,+y quadrant edge: {edge}")
    # #x, -y
    edge = (sx + dd - i, sy - i)
    if edge[1] == row:
        m_lenghts.add(edge)
        log.debug(f"+x,+y quadrant edge: {edge}")
    # #-x,-y
    edge = (sx - dd + i, sy - i)
    if edge[1] == row:
        m_lenghts.add(edge)
        log.debug(f"+x,+y quadrant edge: {edge}")
    log.debug(f"Manhattan lenghts = {m_lenghts}")
    return list(m_lenghts)


def count_non_empty_fields(coords: Dict[Tuple[int, int], str], row: int) -> None:
    count = 0
    for k, v in coords.items():
        x, y = k
        if y == row and v == "#":
            count += 1
    print(f"Total count is {count}")


def find_empty_field(coords: Dict[Tuple[int, int], str]):
    arr = []
    for _ in range(20):
        a = ["."] * 20
        arr.append(a)
    for k, v in coords.items():
        x, y = k
        if x < len(arr) and y < len(arr[0]):
            arr[x][y] = v
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y] == ".":
                print(f"found the spot {x,y}")

def merge_ranges(a: Tuple[int, int], b: List[Tuple[int, int]]) -> List[Tuple[int,int]]:
    if not b:
        return [a]
    # breakpoint()
    a_min,a_max = a
    for i,curr in enumerate(b):
        b_min,b_max = curr
        # new item is smaller
        if a_max < b_min:
            b.insert(i, a)
            return b
        # new item is bigger
        elif a_min > b_max:
            # if last item in b
            if i == (len(b) - 1):
                b.append(a)
                return b
            else:
                continue
        # new item overlaps on left
        elif a_max >= b_min and a_max <= b_max:
            b[i] = (a_min, b_max)
            return b
        # new item overlaps on right
        elif a_min >= b_min and a_max > b_max:
            temp = (b_min, a_max)
            del b[i]
            return merge_ranges(temp, b)
        # new item overlaps on both sides
        else:
            del b[i]
            return merge_ranges(a, b)


def generate_manhatan_ranges(
    list_of_coords: List[Tuple[int, int, int, int]]
    ) -> Dict[int,List[Tuple[int,int]]]:
    map = {}
    for coords in list_of_coords:
        sx, sy, bx, by = coords
        dx = abs(sx - bx)
        log.debug(f"Delta x = {dx}")
        dy = abs(sy - by)
        log.debug(f"Delta y = {dy}")
        dd = dx + dy
        # down -> start for x
        for i in range(dd): # last range element excluded, we will grab it in second loop
            x =  sx - dd + i
            y_min = sy - i
            y_max = sy + i
            # if x < 0 or x > MAX_REGION:
            #     continue
            # if y_min < 0:
            #     y_min = 0
            # if y_max < 0:
            #     y_max = 0
            # if y_min > MAX_REGION:
            #     y_min = MAX_REGION
            # if y_max > MAX_REGION:
            #     y_max = MAX_REGION
            # if y_min == 0 and y_max == 0:
            #     continue
            if x not in map:
                map[x] = [(y_min, y_max)]
            else:
                map[x] = merge_ranges((y_min,y_max), map[x])
        # start -> up range for x 
        for k in range(dd+1): # we include the whole range this time
            x = sx + k
            if x < 0 or x > MAX_REGION:
                continue
            y_min = sy - dd + k
            y_max = sy + dd - k
            if x not in map:
                map[x] = [(y_min, y_max)]
            else:
                map[x] = merge_ranges((y_min,y_max), map[x])
    return map


# we populate a map of ranges that can't have the beacon
def map_ranges(ranges: List[Tuple[int, int, int, int]]) -> Dict[int, List[Tuple[int,int]]]:
    map = {}
    # SETUP
    for r in ranges:
        min_x, max_x, min_y, max_y = r
        y_range = (min_y, max_y)
        # RANGE
        for i in range(min_x, max_x + 1):
            # check map
            if i in map:
                map[i] = merge_ranges(y_range, map[i])
            else:
                map[i] = [y_range]  # wrap in a list
    return map


def invert_map_row(y_range: List[Tuple[int,int]])->List[Tuple[int,Tuple[int,int]]]:
    inverted_ranges = []
    prev = None
    for r in y_range:
        y_min,y_max = r
        # modify ranges
        # if y_min < 0:
        #     y_min = 0
        # if y_max < 0:
        #     y_max = 0
        # if y_min > MAX_REGION:
        #     y_min = MAX_REGION
        # if y_max > MAX_REGION:
        #     y_max = MAX_REGION
        # if y_min == 0 and y_max == 0:
        #     continue
        # if y_min == 0:
        #     prev = (y_max+1, MAX_REGION)
        #     inverted_ranges.append(prev)
        #     continue
        if not prev:
            inverted_ranges.append((0, y_min-1))
            prev = (y_max+1,MAX_REGION)
            inverted_ranges.append(prev)
        else:
            updated_prev = (prev[0], y_min-1)
            inverted_ranges[-1] = updated_prev
            prev = (y_max+1,MAX_REGION)
            inverted_ranges.append(prev)
    return inverted_ranges


def invert_map(map: Dict[int,List[Tuple[int,int]]]) -> Dict[int,List[Tuple[int,int]]]:
    inverted_map = {}
    for x,y_range in map.items():
        inverted = invert_map_row(y_range)
        inverted_map[x] = inverted
    return inverted_map

def print_map(map: Dict[int,List[Tuple[int,int]]] ) -> None:
    matrix = []
    for _ in range(30):
        temp = ['.' for _ in range(30)]
        matrix.append(temp)
    for k,v in map.items():
        for r in v:
            min,max = r
            for i in range(min,max+1):
                matrix[k][i] = '#'
    for row in matrix:
        print(row)



def main(filename):
    parse_args()
    coords = parse_data(filename)
    map = generate_manhatan_ranges(coords)
    count = 0
    for k,v in map.items():
        print(f'{k,v}')
        for range in v:
            min,max = range
            if min <= 10 and max >= 10:
                count += 1
    print(f'There are {count} elements on the row 10')
    print_map(map)

    return
    inverted_map = invert_map(map)
    for k,v in inverted_map.items():
        if len(v) > 1:
            print(f'X = {k}, Y = {v}')


if __name__ == "__main__":
    # main("input")
    # main('sample_input')
    main('small_sample_input')
    # cProfile.run('main("sample_input")',sort='cumtime')
    # cProfile.run('main("input")',sort='cumtime')
