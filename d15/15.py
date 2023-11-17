from typing import Tuple, List
import re
import logging as log
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-log")
log_level = parser.parse_args().log
log.basicConfig(level=log_level)


def parse_line(line: str) -> Tuple[int,int,int,int]:
    pattern = r".*x=(.*),.*y=(.*):.*x=(.*),.*y=(.*)$"
    m = re.search(pattern, line)
    if m:
        sx, sy, bx, by = m.groups()
        sx, sy, bx, by = int(sx), int(sy), int(bx), int(by)
        log.info(f"sx = {sx}, sy={sy}, bx={bx}, by={by}")
        return sx, sy, bx, by
    else:
        print("no match")
    raise Exception(f'Failed to parse the input: \n{line}')


def parse_data(filename) -> List[Tuple[int,int,int,int]]:
    f = open(filename, "r")
    data = f.read().strip()
    lines = data.split("\n")
    coords = []
    for l in lines:
        c = parse_line(l)
        coords.append(c)
    return coords


def generate_manhatan_lengths(coords: Tuple[int,int,int,int]):
    pass


def main(filename):
    C = set()
    coords = parse_data(filename)
    for c in coords:
        m_lens = generate_manhatan_lengths(c)



if __name__ == "__main__":
    # main("input")
    main('sample_input')
