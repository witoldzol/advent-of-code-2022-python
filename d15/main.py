import enum
from typing import Tuple, List, Dict
import re
import logging as log
import argparse


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


def generate_manhatan_lengths(coords: Tuple[int, int, int, int]):
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
    for i, d in enumerate(range(dd, -1, -1)):
        # x ,y
        edge = (sx + dd - i, sy + i)
        log.debug(f"index = {i}, range = {d}")
        log.debug(f"+x,+y quadrant edge: {edge}")
        m_lenghts.add(edge)
        # -x, y
        edge = (sx - dd + i, sy + i)
        log.debug(f"index = {i}, range = {d}")
        log.debug(f"+x,+y quadrant edge: {edge}")
        m_lenghts.add(edge)
        # #x, -y
        edge = (sx + dd - i, sy - i)
        log.debug(f"index = {i}, range = {d}")
        log.debug(f"+x,+y quadrant edge: {edge}")
        m_lenghts.add(edge)
        # #-x,-y
        edge = (sx - dd + i, sy - i)
        log.debug(f"index = {i}, range = {d}")
        log.debug(f"+x,+y quadrant edge: {edge}")
        m_lenghts.add(edge)
    log.debug(f"Manhattan lenghts = {m_lenghts}")
    print(f"Manhattan lenghts = {m_lenghts}")
    return list(m_lenghts)


def fill_the_borders(borders: Dict[Tuple[int, int], str]):
    # iterate over map, find start (min x)and end(max x) of each row (y axis)
    # then, fill out all 'empty' row fields
    row_min_max = {}
    for k, v in borders.items():
        # min max x for each y
        # dict of key = y, (min,max) x
        x, y = k
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
            if (x, y) not in borders:
                borders[(x, y)] = "#"


def print_matrix(coords: Dict[Tuple[int, int], str]):
    n = 35
    matrix = [["."] * n for _ in range(n)]
    for k, v in coords.items():
        x, y = k
        try:
            matrix[x][y] = v
        except Exception as e:
            print(e)
            print("==============")
            print(f"coords = {x},{y}")
    for row in matrix:
        print(row)


def count_non_empty_fields(coords: Dict[Tuple[int, int], str], row: int) -> None:
    count = 0
    for k, v in coords.items():
        x, y = k
        if y == row and v == "#":
            count += 1
    print(f"Total count is {count}")


def main(filename):
    parse_args()
    C = {}
    coords = parse_data(filename)
    for c in coords:
        sx, sy, bx, by = c
        C[(sx, sy)] = "S"
        C[(bx, by)] = "B"
    for c in coords[6:7]:
        print(f"COOOORS : {c}")
        sx, sy, bx, by = c
        C[(sx, sy)] = "S"
        C[(bx, by)] = "B"
        m_lens = generate_manhatan_lengths(c)
        # create outline
        for l in m_lens:
            if l not in C:
                C[l] = "#"
        # fill out the rest of the fields inside the outline created by the lenghts
    fill_the_borders(C)
    print_matrix(C)
    row = 10
    count_non_empty_fields(C, row)


if __name__ == "__main__":
    # main("input")
    main("sample_input")
    # main("small_sample_input")
