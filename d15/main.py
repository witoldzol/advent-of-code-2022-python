from typing import Tuple, List, Dict
import re
import logging as log
import argparse
import pudb
import cProfile
from pstats import SortKey


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


def merge_ranges(a: Tuple[int, int], b: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    if not b:
        return [a]
    a_min, a_max = a
    for i, curr in enumerate(b):
        b_min, b_max = curr
        # new item is inside of old item
        # ba ab
        if b_min <= a_min and a_max <= b_max:
            return b
        # new item is adjecent on the left
        elif a_max == (b_min - 1):
            del b[i]
            return merge_ranges((a_min, b_max), b)
        # new item is smaller
        elif a_max < b_min:
            b.insert(i, a)
            return b
        # new item is adjecent on the right
        elif (a_min - 1) == b_max:
            temp = (b_min, a_max)
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
        elif a_min <= b_min and a_max >= b_min and a_max <= b_max:
            b[i] = (a_min, b_max)
            return b
        # new item overlaps on right
        elif a_min >= b_min and a_max > b_max:
            temp = (b_min, a_max)
            del b[i]
            return merge_ranges(temp, b)
        # new item overlaps on both sides
        # ab ba
        elif a_min <= b_min and b_max <= a_max:
            del b[i]
            return merge_ranges(a, b)
        else:
            raise Exception("Unknown case")


def generate_manhatan_ranges_orig(
    list_of_coords: List[Tuple[int, int, int, int]]
) -> Dict[int, List[Tuple[int, int]]]:
    map = {}
    for coords in list_of_coords:
        sx, sy, bx, by = coords
        dx = abs(sx - bx)
        dy = abs(sy - by)
        dd = dx + dy
        # down -> start for x
        start = 0
        end = dd
        # if sx is negative, we can skip this portion, as we will always be under 0 line
        if sx > 0:
            # set min X bound
            if sx - dd < 0:
                start = dd - sx
            # set max X bound
            if sx > MAX_REGION and (sx - dd) < MAX_REGION:
                end = sx - dd
            for i in range(start, end):
                x = sx - dd + i
                y_min = sy - i
                y_max = sy + i
                # limit Y
                if y_max <= 0:
                    continue
                if y_min >= MAX_REGION:
                    continue
                if y_min < 0:
                    y_min = 0
                if y_max > MAX_REGION:
                    y_max = MAX_REGION
                if x not in map:
                    map[x] = [(y_min, y_max)]
                else:
                    map[x] = merge_ranges((y_min, y_max), map[x])
        # start -> up range for x
        end = dd
        if sx < MAX_REGION:
            if sx + dd > MAX_REGION:
                end = MAX_REGION - sx
            for k in range(end + 1):  # we include the whole range this time
                x = sx + k
                y_min = sy - dd + k
                y_max = sy + dd - k
                # limit Y
                if y_max <= 0:
                    continue
                if y_min >= MAX_REGION:
                    continue
                if y_min < 0:
                    y_min = 0
                if y_max > MAX_REGION:
                    y_max = MAX_REGION
                if x not in map:
                    map[x] = [(y_min, y_max)]
                else:
                    map[x] = merge_ranges((y_min, y_max), map[x])
    return map

def generate_manhatan_ranges( list_of_coords):
    consty = 10
    # consty = 2000000
    X = set(range(-int(1e5),int(1e5)))
    B = set()
    x_len = len(X)
    count = 0
    for coords in list_of_coords:
        print(coords)
        sx, sy, bx, by = coords
        dx = abs(sx - bx)
        dy = abs(sy - by)
        dd = dx + dy
        to_remove = []
        if by == consty:
            B.add(bx)
        for x in X:
            ddd = abs(x-sx)+abs(consty-sy)
            if ddd <= dd:
                to_remove.append(x)
        for x in to_remove:
            X.remove(x)
    for b in B:
        X.add(b)
    print(x_len - len(X))




def print_map(map: Dict[int, List[Tuple[int, int]]]) -> None:
    matrix = []
    for _ in range(30):
        temp = ["." for _ in range(30)]
        matrix.append(temp)
    for k, v in map.items():
        for r in v:
            min, max = r
            for i in range(min, max + 1):
                matrix[k][i] = "#"
    for row in matrix:
        print(row)


def is_there_a_beacon_on_row(coords: List[Tuple[int, int, int, int]], row: int) -> int:
    count = 0
    unique_beacons = set()
    for c in coords:
        sx, sy, bx, by = c
        unique_beacons.add((bx, by))
    for b in unique_beacons:
        x, y = b
        if y == row:
            count += 1
    return count


def main_orig(filename):
    parse_args()
    coords = parse_data(filename)
    map = generate_manhatan_ranges(coords)
    for k, v in map.items():
        if len(v) > 1:
            first, _ = v
            print(f"{v=}")
            f_min, f_max = first
            point_out_of_bounds = f_max + 1
            print(f"{point_out_of_bounds=}")
            tuning = (k * MAX_REGION) + point_out_of_bounds
            print(f"Tuning point is = {tuning}")

def main(filename):
    parse_args()
    coords = parse_data(filename)
    generate_manhatan_ranges(coords)


if __name__ == "__main__":
    # cProfile.run('main("input")', sort=SortKey.CALLS)
    input = "small_sample_input"
    input = 'sample_input'
    # input = "input"
    if input == "sample_input" or input == "small_sample_input":
        ROW = 10
        MAX_REGION = 20
    else:
        ROW = 2000000
        MAX_REGION = 4_000_000
    result = main(input)
    # if input == 'sample_input':
    #     assert result == 26
    # else:
    #     assert result == 4737567
    # # main('small_sample_input')
