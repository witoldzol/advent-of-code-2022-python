# todo -> fltten the returned paths ?
# refactor duplicated code 
# paths take counter (int) and list of ints, line 44, investigate
# each node can go to 3 directions only ( 4 minus the origin )
# how can we reuse & remember 'dead end' paths so that we can avoid pursuing them in the future?
# 0,0 -> we have 2 options -> take 0,1, we have 2 options -> 0,2 -> we have ... 0,n -> we can't go anywhere ( REMEMBER ? ) 
# but each path has multiple branches, some of which we didn't explore yet, how do we capture that?
# depth first search, with recursion
# breadth first search ? it is best suited for shortest path -> this is a shortest path problem !!
from collections import namedtuple
from typing import List, Dict

Direction = namedtuple('Direction', "x y") 

def main(filename):
    start = Direction(0,0)
    matrix = build_matrix(filename) 
    print(matrix)
    paths = traverse(matrix, start, {}, 0, [], [])
    filtered_paths = {i for i in paths if type(i) is int}
    fastest_path = min(filtered_paths)
    print('fastest path is :' , fastest_path)


def build_matrix(filename: str) -> List[List[str]]:
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            matrix.append(list(line))
    return matrix


def traverse(matrix: List[List[str]], start: Direction, visited: Dict[str,bool], counter: int, path: List[str], paths: List) -> List[int]:
    print(f'Visiting {start.x},{start.y}')
    path.append(f'{start.x},{start.y}')
    counter += 1
    # print(f'counter is {counter}')
    # print(f'len {len(path)}\n {path}')
    visited[str(start)] = True
    visited_new = visited.copy()
    directions: List[Direction] = get_valid_directions(matrix, start, visited_new)
    if not directions:
        print('',end='')#print(f'current location: {start.x},{start.y} - there are no valid directions left')
        return []
    # base condition
    for d in directions:
        if matrix[d.x][d.y] == 'E':
            print('',end='')#print(f'Found the end - counter is {counter}')
            paths.append(counter)
            return paths
    valid_dirs = [f'{d.x},{d.y}' for d in directions]
    print('',end='')#print(f'valid direction : {valid_dirs}')
    for d in directions:
        new_path = path.copy()
        paths.append(traverse(matrix, d, visited_new, counter, new_path, paths))
    return paths

def translate_start_and_end_cells(neighbour_cell: str) -> str:
    if neighbour_cell == 'E':
        neighbour_cell = 'z'
    if neighbour_cell == 'S':
        neighbour_cell = '|' # | is the 2 chars after z, and will always be 'higher than start cell ( hence S will never be valid direction)
    return neighbour_cell


def get_valid_directions(matrix: List[List[str]], start: Direction, visited: Dict[str,bool]) -> List[Direction]:
    start_value = matrix[start.x][start.y]
    if start_value == 'S':
        start_value = 'a'
    valid_directions: List[Direction] = []
    direction = 'UP'
    up = start.x - 1
    if up < 0:
        pass
        print('',end='')#print(f'Going {direction} to {up},{start.y} is off bounds')
    else:
        neighbour_cell = matrix[up][start.y]  
        neighbour_cell = translate_start_and_end_cells(neighbour_cell)
        print('',end='')#print(f' ord of neightbour cell == {ord(neighbour_cell)} ord of start value {(ord(start_value) + 1)}')
        if ord(neighbour_cell) <= (ord(start_value) + 1):
            print('',end='')#print(f'start: {start.x},{start.y} {start_value} is higher or equal than {direction} {up},{start.y} [{matrix[up][start.y]}]')
            if str(Direction(up,start.y)) in visited:
                print('',end='')#print(f'Direction {str(Direction(up,start.y))} was already visited')
            else:
                valid_directions.append(Direction(up, start.y))
        else:
            pass
            print('',end='')#print(f'start: {start.x},{start.y} [{start_value}] is lower than {direction} {up},{start.y} [{matrix[up][start.y]}]')
    direction = 'DOWN'
    down = start.x + 1
    if down >= len(matrix):
        print('',end='')#print(f'Going {direction} to {down},{start.y} is off bounds')
    else:
        neighbour_cell = matrix[down][start.y]  
        neighbour_cell = translate_start_and_end_cells(neighbour_cell)
        print('',end='')#print(f' ord of neightbour cell == {ord(neighbour_cell)} ord of start value {(ord(start_value) + 1)}')
        if ord(neighbour_cell) <= (ord(start_value) + 1):
            print('',end='')#print(f'start: {start.x},{start.y} [{start_value}] is higher or equal than {direction} {down},{start.y} [{matrix[down][start.y]}]')
            if str(Direction(down,start.y)) in visited:
                print('',end='')#print(f'Direction {str(Direction(down,start.y))} was already visited')
            else:
                valid_directions.append(Direction(down, start.y))
        else:
            print('',end='')#print(f'start: {start.x},{start.y} [{start_value}] is lower than {direction} {down},{start.y} [{matrix[down][start.y]}]')
    direction = 'LEFT'
    left = start.y - 1
    if left < 0:
        print('',end='')#print(f'Going {direction} to {start.x},{left} is off bounds')
    else:
        neighbour_cell = matrix[start.x][left]  
        neighbour_cell = translate_start_and_end_cells(neighbour_cell)
        print('',end='')#print(f' ord of neightbour cell == {ord(neighbour_cell)} ord of start value {(ord(start_value) + 1)}')
        if ord(neighbour_cell) <= (ord(start_value) + 1):
            print('',end='')#print(f'start: {start.x},{start.y} [{start_value}] is higher or equal than {direction} {start.x},{left} [{matrix[start.x][left]}]')
            if str(Direction(start.x,left)) in visited:
                print('',end='')#print(f'Direction {str(Direction(start.x,left))} was already visited')
            else:
                valid_directions.append(Direction(start.x, left))
        else:
            print('',end='')#print(f'start: {start.x},{start.y} [{start_value}] is lower than {direction} {start.x},{left} [{matrix[start.x][left]}]')
    direction = 'RIGHT'
    right = start.y + 1
    if right >= len(matrix[0]):
        print('',end='')#print(f'Going {direction} to {start.x},{right} is off bounds')
    else:
        neighbour_cell = matrix[start.x][right]  
        neighbour_cell = translate_start_and_end_cells(neighbour_cell)
        print('',end='')#print(f' ord of neightbour cell == {ord(neighbour_cell)} ord of start value {(ord(start_value) + 1)}')
        if ord(neighbour_cell) <= (ord(start_value) + 1):
            print('',end='')#print(f'start: {start.x},{start.y} [{start_value}] is higher or equal than {direction} {start.x},{right} [{matrix[start.x][right]}]')
            if str(Direction(start.x,right)) in visited:
                print('',end='')#print(f'Direction {str(Direction(start.x,right))} was already visited')
            else:
                valid_directions.append(Direction(start.x, right))
        else:
            print('',end='')#print(f'start: {start.x},{start.y} [{start_value}] is lower than {direction} {start.x},{right} [{matrix[start.x][right]}]')
    return valid_directions


if __name__ == "__main__":
   main('sample_input')
