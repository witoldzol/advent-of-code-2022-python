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
        log.debug(f"sx = {sx}, sy={sy}, bx={bx}, by={by}")
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
    m_lenghts = []
    sx, sy, bx, by = coords
    dx=abs(sx-bx)
    dy=abs(sy-by)
    dd = max(dx,dy)
    for x in range(0, dd+1):
        m_lenghts.append((x,dd-x))
    for x in range(-dd,1):
        m_lenghts.append((x,dd+x))
    for y in range(0, dd+1):
        m_lenghts.append((dd-y,y))
    for y in range(-dd,1):
        m_lenghts.append((dd+y,y))
    return m_lenghts


def main(filename):
    C = set()
    coords = parse_data(filename)
    # for c in coords:
    lens = {}
    for c in coords[6:7]:
        m_lens = generate_manhatan_lengths(c)
        for l in m_lens:
            x,y = l
            print(x,y)





if __name__ == "__main__":
    # main("input")
    main('sample_input')
