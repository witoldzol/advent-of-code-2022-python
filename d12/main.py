from collections import namedtuple
from typing import List

Direction = namedtuple('Direction', "x y") 

def main(filename):
    start = Direction(0,0)
    matrix = build_matrix(filename) 
    print(matrix)
    print(f'steps to zenit = {traverse(matrix, start, [], 0)}')


def build_matrix(filename: str) -> List[List[str]]:
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            matrix.append(list(line))
    return matrix


def traverse(matrix: List[List[str]], start: Direction, visited: List[Direction], counter: int = 0) -> int:
    # check all adjecent cells
    # loop over valid ones 
    # each call will be recursive
    # pass location from where you came, to avoid backtracking
    visited.append(start)
    paths = []
    directions: List[Direction] = get_valid_directions(matrix, start)
    # base condition
    for d in directions:
        if matrix[d.x][d.y] == 'E':
            counter += 1
            return counter
    for d in directions:
        if d in visited:
            # print(f'this node has been visited {d.x},{d.y}')
            directions.remove(d)
    for d in directions:
        counter += 1
        paths.append(traverse(matrix, d, visited, counter))
    return -1


def get_valid_directions(matrix: List[List[str]], start: Direction) -> List[Direction]:
    start_value = matrix[start.x][start.y]
    if start_value == 'S':
        start_value = 'a'
    elif start_value == 'E':
        print('==========================================')
        print('FOUND END!!!!!!!!!!!!!!!!!!')
        print('==========================================')
        start_value = 'z'
    valid_directions: List[Direction] = []
    direction = 'UP'
    up = start.x - 1
    if up < 0:
        pass
        #print(f'Going {direction} to {up},{start.y} is off bounds')
    else:
        if matrix[up][start.y] >= start_value:
            #print(f'start: {start.x},{start.y} {start_value} is lower or equal than {direction} {up},{start.y} [{matrix[up][start.y]}]')
            valid_directions.append(Direction(up, start.y))
        else:
            pass
            #print(f'start: {start.x},{start.y} [{start_value}] is higher than {direction} {up},{start.y} [{matrix[up][start.y]}]')
    direction = 'DOWN'
    down = start.x + 1
    if down >= len(matrix):
        pass
        #print(f'Going {direction} to {down},{start.y} is off bounds')
    else:
        if matrix[down][start.y] >= start_value:
            #print(f'start: {start.x},{start.y} [{start_value}] is lower or equal than {direction} {down},{start.y} [{matrix[down][start.y]}]')
            valid_directions.append(Direction(down, start.y))
        else:
            pass
            #print(f'start: {start.x},{start.y} [{start_value}] is higher than {direction} {down},{start.y} [{matrix[down][start.y]}]')
    direction = 'LEFT'
    left = start.y - 1
    if left < 0:
        pass
        #print(f'Going {direction} to {start.x},{left} is off bounds')
    else:
        if matrix[start.x][left] >= start_value:
            #print(f'start: {start.x},{start.y} [{start_value}] is lower or equal than {direction} {start.x},{left} [{matrix[start.x][left]}]')
            valid_directions.append(Direction(start.x, left))
        else:
            pass
            #print(f'start: {start.x},{start.y} [{start_value}] is higher than {direction} {start.x},{left} [{matrix[start.x][left]}]')
    direction = 'RIGHT'
    right = start.y + 1
    if right >= len(matrix[0]):
        pass
        #print(f'Going {direction} to {start.x},{right} is off bounds')
    else:
        if matrix[start.x][right] >= start_value:
            #print(f'start: {start.x},{start.y} [{start_value}] is lower or equal than {direction} {start.x},{right} [{matrix[start.x][right]}]')
            valid_directions.append(Direction(start.x, right))
        else:
            pass
            #print(f'start: {start.x},{start.y} [{start_value}] is higher than {direction} {start.x},{right} [{matrix[start.x][right]}]')
    return valid_directions


if __name__ == "__main__":
   main('sample_input')
