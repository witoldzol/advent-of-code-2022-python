from collections import namedtuple
from typing import List

Direction = namedtuple('Direction', "x y") 

def main(filename):
    start = Direction(0,0)
    end = Direction(2,5)
    matrix = build_matrix(filename) 
    print(matrix)
    return traverse(matrix, start, end)


def build_matrix(filename: str) -> List[List[str]]:
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            matrix.append(list(line))
    return matrix


def traverse(matrix: List[List[str]], start: Direction, end: Direction) -> int:
    # check all adjecent cells
    # loop over valid ones 
    # each call will be recursive
    # pass location from where you came, to avoid backtracking
    directions: List[Direction] = get_valid_directions(matrix, start)
    return 31


def get_valid_directions(matrix: List[List[str]], start: Direction) -> List[Direction]:
    print(start.x)
    print(start.y)
    return list(Direction(1,1))


if __name__ == "__main__":
    main('sample_input')
