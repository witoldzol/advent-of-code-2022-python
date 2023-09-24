# breadth first search is optimal for finding shortest path
# don't use recursion, it's much slower!
# ie. highest directions should be first, so we end up going up first whenever we have a chance
from collections import namedtuple
from typing import List, Dict
from queue import Queue

Direction = namedtuple('Direction', "x y") 

class Cell:
    x: int
    y: int
    v: int
    
    def __init__(self, x:int, y:int, v:str):
        self.x = x
        self.y = y
        self.v = ord(v)

def main(filename):
    start = Direction(0,0)
    start_cell = Cell(0,0,'a')
    matrix = build_matrix(filename) 
    path = breadth_traverse(matrix, start, start_cell)
    print('path is : ' , list(reversed(path)))
    print(f'steps => {len(path)}')


def build_matrix(filename: str) -> List[List[str]]:
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            matrix.append(list(line))
    return matrix


def is_end(matrix, d):
    if matrix[d.x][d.y] == 'E':
        print(f'Found ending at {d.x},{d.y}')
        return True
    

def breadth_traverse(matrix: List[List[str]], start: Direction, start_cell: Cell) -> List[str]:
    path: List[str] = []
    count = 0
    visited: Dict[str,bool] = {}
    next_to_visit: Queue = Queue()
    valid_directions: List[Direction] = get_valid_directions(matrix, start, visited, start_cell)
    # init queue
    for d in valid_directions:
        next_to_visit.put(d)
    parent_map = {}
    for d in iter(next_to_visit.get, None):
        parent = d
        count += 1
        print(f'visiting {str(d)}')
        if str(d) in visited:
            continue
        visited[str(d)] = True
        cell = Cell(d.x,d.y,matrix[d.x][d.y])
        valid_directions: List[Direction] = get_valid_directions(matrix, d, visited, cell)
        # check if end found
        for d in valid_directions:
            if is_end(matrix, d):
                parent_map[str(d)] = str(parent)
                path = trace_back_path(d, parent_map)
                return path
            if str(d) not in visited:
                parent_map[str(d)] = str(parent)
                next_to_visit.put(d)
    return path


def trace_back_path(end: Direction, map: Dict[str,str]) -> List[str]:
    path = []
    path.append(str(end))
    current = str(end)
    while current in map:
        parent: str = map[current]
        path.append(parent)
        current = parent 
    return path


def translate_start_and_end_cells(neighbour_cell: str) -> str:
    if neighbour_cell == 'E':
        neighbour_cell = 'z'
    if neighbour_cell == 'S':
        neighbour_cell = '|' # | is the 2 chars after z, and will always be 'higher than start cell ( hence S will never be valid direction)
    return neighbour_cell


def get_valid_directions(matrix: List[List[str]], start: Direction, visited: Dict[str,bool], start_cell: Cell) -> List[Direction]:
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
                print(f'Direction {str(Direction(up,start.y))} was already visited')
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
                print(f'Direction {str(Direction(down,start.y))} was already visited')
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
                print(f'Direction {str(Direction(start.x,left))} was already visited')
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
                print(f'Direction {str(Direction(start.x,right))} was already visited')
                print('',end='')#print(f'Direction {str(Direction(start.x,right))} was already visited')
            else:
                valid_directions.append(Direction(start.x, right))
        else:
            print('',end='')#print(f'start: {start.x},{start.y} [{start_value}] is lower than {direction} {start.x},{right} [{matrix[start.x][right]}]')
    return valid_directions


if __name__ == "__main__":
   main('sample_input')
   # main('input')
