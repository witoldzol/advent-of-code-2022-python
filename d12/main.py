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
    direction = 'UP'
    up = start.x - 1
    if up < 0:
        print(f'Going {direction} to {up},{start.y} is off bounds')
    else:
        if matrix[up][start.y] > matrix[start.x][start.y]:
            print(f'start: {start.x},{start.y} is lower than {direction} {up}{start.y}')
        else:
            print(f'start: {start.x},{start.y} is higher or equal than {direction} {up},{start.y}')
    direction = 'DOWN'
    down = start.x + 1
    if down < 0:
        print(f'Going {direction} to {down},{start.y} is off bounds')
    else:
        if matrix[down][start.y] > matrix[start.x][start.y]:
            print(f'start: {start.x},{start.y} is lower than {direction} {down}{start.y}')
        else:
            print(f'start: {start.x},{start.y} is higher or equal than {direction} {down},{start.y}')
    direction = 'LEFT'
    left = start.y - 1
    if up < 0:
        print(f'Going {direction} to {start.x},{left} is off bounds')
    else:
        if matrix[start.x][left] > matrix[start.x][start.y]:
            print(f'start: {start.x},{start.y} is lower than {direction} {start.x}{left}')
        else:
            print(f'start: {start.x},{start.y} is higher or equal than {direction} {start.x},{left}')
    direction = 'RIGHT'
    right = start.y + 1
    if up < 0:
        print(f'Going {direction} to {start.x},{right} is off bounds')
    else:
        if matrix[start.x][right] > matrix[start.x][start.y]:
            print(f'start: {start.x},{start.y} is lower than {direction} {start.x}{right}')
        else:
            print(f'start: {start.x},{start.y} is higher or equal than {direction} {start.x},{right}')

    return list(Direction(1,1))


if __name__ == "__main__":
    main('sample_input')
