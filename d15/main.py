import cProfile
from typing import Tuple, List, Dict
import re
import logging as log
import argparse
import numpy as np


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


def generate_manhatan_lengths_slow(coords: Tuple[int, int, int, int]) -> List[Tuple[int,int]]:
    sx,sy,bx,by = coords
    dx = sx - bx
    dy = sy - by
    dd = abs(dx) + abs(dy)
    if not dd:
        return []
    ml = set()
    for i in range(0,dd+1):
        # x,y
        c = (sx+i,sy+dd-i)
        ml.add(c)
        # -x, y
        c = (sx-i,sy+dd-i)
        ml.add(c)
        # x, -y
        c = (sx+dd-i,sy-i)
        ml.add(c)
        # -x, -y
        c = (sx-dd+i,sy-i)
        ml.add(c)
    return list(ml)

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
    print(f"{i=}")
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


def print_matrix(coords: Dict[Tuple[int, int], str]):
    n = 20
    matrix = [["."] * n for _ in range(n)]
    for k, v in coords.items():
        x, y = k
        try:
            matrix[x][y] = v
        except Exception:
            pass
    for row in matrix:
        print(row)


def count_non_empty_fields(coords: Dict[Tuple[int, int], str], row: int) -> None:
    count = 0
    for k, v in coords.items():
        x, y = k
        if y == row and v == "#":
            count += 1
    print(f"Total count is {count}")


def fill_the_borders2(coords, lens: List[Tuple[int, int]]):
    row_min_max = {}
    for l in lens:
        x, y = l
        if y not in row_min_max:
            row_min_max[y] = (x, None)
        else:
            min, max = row_min_max[y]  # max is always None
            if x < min:
                row_min_max[y] = (x, min)
            else:
                row_min_max[y] = (min, x)
    for y, v in row_min_max.items():
        start_x, end_x = v
        if not end_x:
            end_x = start_x
        for x in range(start_x, end_x):
            if (x, y) not in coords:
                coords[(x, y)] = "#"

def find_empty_field(coords: Dict[Tuple[int,int],str]):
    arr = []
    for _ in range(20):
        a = ['.'] * 20
        arr.append(a)
    for k,v in coords.items():
        x,y = k
        if x < len(arr) and y < len(arr[0]):
            arr[x][y] = v
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y] == '.':
                print(f'found the spot {x,y}')


def main(filename):
    parse_args()
    C = {}
    coords = parse_data(filename)
    for c in coords:
        sx, sy, bx, by = c
        C[(sx, sy)] = "S"
        C[(bx, by)] = "B"
    for c in coords:
        sx, sy, bx, by = c
        C[(sx, sy)] = "S"
        C[(bx, by)] = "B"
        # m_lens = generate_manhatan_lengths(c, ROW)
        m_lens = generate_manhatan_lengths_slow(c)
        # create outline
        for l in m_lens:
            if l not in C:
                C[l] = "#"
        # fill out the rest of the fields inside the outline created by the lenghts
        fill_the_borders2(C, m_lens)
    print_matrix(C)
    # count_non_empty_fields(C, ROW)
    find_empty_field(C)


# ROW = 2000000
ROW = 10

if __name__ == "__main__":
    main('sample_input')
    # main('small_sample_input')
    # cProfile.run('main("sample_input")',sort='cumtime')
    # cProfile.run('main("input")',sort='cumtime')
