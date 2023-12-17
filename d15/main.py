from typing import Tuple, List, Dict
import re
import logging as log
import argparse
import pudb
import cProfile
from pstats import SortKey

# def invert_map_row(y_range: List[Tuple[int,int]])->List[Tuple[int,Tuple[int,int]]]:
#     inverted_ranges = []
#     prev = None
#     for r in y_range:
#         y_min,y_max = r
#         # modify ranges
#         # if y_min < 0:
#         #     y_min = 0
#         # if y_max < 0:
#         #     y_max = 0
#         # if y_min > MAX_REGION:
#         #     y_min = MAX_REGION
#         # if y_max > MAX_REGION:
#         #     y_max = MAX_REGION
#         # if y_min == 0 and y_max == 0:
#         #     continue
#         # if y_min == 0:
#         #     prev = (y_max+1, MAX_REGION)
#         #     inverted_ranges.append(prev)
#         #     continue
#         if not prev:
#             inverted_ranges.append((0, y_min-1))
#             prev = (y_max+1,MAX_REGION)
#             inverted_ranges.append(prev)
#         else:
#             updated_prev = (prev[0], y_min-1)
#             inverted_ranges[-1] = updated_prev
#             prev = (y_max+1,MAX_REGION)
#             inverted_ranges.append(prev)
#     return inverted_ranges
#
#
# def invert_map(map: Dict[int,List[Tuple[int,int]]]) -> Dict[int,List[Tuple[int,int]]]:
#     inverted_map = {}
#     for x,y_range in map.items():
#         inverted = invert_map_row(y_range)
#         inverted_map[x] = inverted
#     return inverted_map

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


def merge_ranges(a: Tuple[int, int], b: List[Tuple[int, int]]) -> List[Tuple[int,int]]:
    if not b:
        return [a]
    a_min,a_max = a
    for i,curr in enumerate(b):
        b_min,b_max = curr
        # new item is inside of old item
        if a_min > b_min and a_max < b_max:
            return b
        # new item is adjecent on the left
        elif a_max == (b_min - 1):
            del b[i]
            return merge_ranges((a_min,b_max),b)
        # new item is smaller
        elif a_max < b_min:
            b.insert(i, a)
            return b
        # new item is adjecent on the right
        elif (a_min - 1) == b_max:
            temp = (b_min,a_max)
            del b[i]
            return merge_ranges(temp, b)
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
        dy = abs(sy - by)
        dd = dx + dy
        # down -> start for x
        for i in range(dd): # last range element excluded, we will grab it in second loop
            x =  sx - dd + i # can change range to pre calc X, but then we need to calc i 
            y_min = sy - i # if we move from 0-dd, to min-x to max-x, then we need to figure out starting i to plug into y range calc
            y_max = sy + i # we also need to check if this makes sense, ie do this only for ranges that go out of bounds for X (0-MAX_REGION)
            # narrow range
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
            # do work
            if x not in map:
                map[x] = [(y_min, y_max)]
            else:
                map[x] = merge_ranges((y_min,y_max), map[x])
        # start -> up range for x 
        for k in range(dd+1): # we include the whole range this time
            x = sx + k
            y_min = sy - dd + k
            y_max = sy + dd - k
            # narrow range
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
            # do work
            if x not in map:
                map[x] = [(y_min, y_max)]
            else:
                map[x] = merge_ranges((y_min,y_max), map[x])
    return map


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


def is_there_a_beacon_on_row(coords: List[Tuple[int,int,int,int]], row: int) -> int:
    count = 0
    unique_beacons = set()
    for c in coords:
        sx, sy, bx, by = c
        unique_beacons.add((bx,by))
    for b in unique_beacons:
        x,y = b
        if y == row:
            count += 1
    return count


def main(filename):
    parse_args()
    coords = parse_data(filename)
    map = generate_manhatan_ranges(coords)
    count = 0
    # count the items on row
    for k,v in map.items():
        # print(f'{k,v}')
        for r in v:
            min,max = r
            if min <= ROW and max >= ROW:
                count += 1
    print(f'There are {count} elements on the row {ROW}')
    beacons = is_there_a_beacon_on_row(coords, ROW)
    if beacons:
        count -= beacons
        print(f'There is/are {beacons} beacon(s) on row {ROW } so we lower count by one. Final count =  {count}')
    return count

    # print_map(map)
    inverted_map = invert_map(map)
    for k,v in inverted_map.items():
        if len(v) > 1:
            print(f'X = {k}, Y = {v}')


ROW = 10
# ROW = 2000000
if __name__ == "__main__":
    # cProfile.run('main("input")', sort=SortKey.CALLS)
    input = 'sample_input'
    # input = 'input'
    result = main(input)
    if input == 'sample_input':
        assert result == 26
    else:
        assert result == 4737567
    # main('small_sample_input')
