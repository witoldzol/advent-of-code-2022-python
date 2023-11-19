from typing import Tuple, List, Dict
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
    for x in range(sx, sx+dd+1):
        m_lenghts.append((x,dd-x))
    for x in range(-dd-sx,sx+1):
        m_lenghts.append((x,dd+x))
    for y in range(sy, sy+dd+1):
        m_lenghts.append((dd-y,y))
    for y in range(-dd-sy,sy+1):
        m_lenghts.append((dd+y,y))
    return m_lenghts

def print_matrix(coords: Dict[Tuple[int,int],str]):
    matrix = [ ['.']*25 for _ in range(25)]
    for k,v in coords.items():
        x,y = k
        try:
            matrix[x][y] = v
        except Exception as e:
            print(e)
            print('==============')
            print(f'coords = {x},{y}')
    for row in matrix:
        print(row)



def main(filename):
    C = {}
    coords = parse_data(filename)
    # for c in coords:
    for c in coords[6:7]:
        sx,sy,bx,by = c
        C[(sx,sy)] = 'S'
        C[(bx,by)] = 'B'
        m_lens = generate_manhatan_lengths(c)
        for l in m_lens:
            if l not in C:
                C[l] = '#'
    # print(C)
    print_matrix(C)


if __name__ == "__main__":
    # main("input")
    main('sample_input')
