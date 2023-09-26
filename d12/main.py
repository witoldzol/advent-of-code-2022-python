from collections import namedtuple
from typing import List, Dict, Tuple
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

    def __str__(self) -> str:
        return f'{self.x},{self.y}'


    def __repr__(self) -> str:
        return f'Cell(x={self.x},y={self.y},v={self.v})'


def main(filename):
    start = Direction(0,0)
    matrix = build_matrix(filename) 
    start = find_start(matrix)
    start_direction = Direction(start[0], start[1])
    start_cell = Cell(start[0],start[1],'a')
    path = breadth_traverse(matrix, start_direction, start_cell)
    print(f'steps => {len(path)}')
    visualise_path(len(matrix), len(matrix[0]), path)


def find_start(matrix: List[List[str]]) -> Tuple[int,int]:
    for x, row in enumerate(matrix):
        for y, cell in enumerate(row):
            if cell == 'S':
                return x,y
    return 0,0


def visualise_path(x: int, y: int, path: List[str]) -> None:
    matrix = []
    for _ in range(x):
        temp = []
        for _ in range(y):
            temp.append('.')
        matrix.append(temp)
    for cell in path:
        x,y = cell.split(',')
        matrix[int(x)][int(y)] = '='
    for row in matrix:
        r = ''.join(row)
        print(r)

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
    valid_directions: List[Cell] = get_valid_directions2(matrix, start, visited, start_cell)
    # init queue
    for d in valid_directions:
        next_to_visit.put(d)
    parent_map = {}
    for d in iter(next_to_visit.get, None):
        cell = Cell(d.x,d.y,matrix[d.x][d.y])
        parent = d
        count += 1
        if str(cell) in visited:
            continue
        visited[str(cell)] = True
        valid_directions: List[Cell] = get_valid_directions2(matrix, d, visited, cell)
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


def trace_back_path(end: Cell, map: Dict[str,str]) -> List[str]:
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


def get_valid_directions2(matrix: List[List[str]], start: Direction, visited: Dict[str,bool], start_cell: Cell) -> List[Cell]:
    valid_directions: List[Cell] = []
    up = start.x - 1
    if not up < 0:
        neighbour_cell = matrix[up][start.y]  
        neighbour_cell = translate_start_and_end_cells(neighbour_cell)
        target_cell: Cell = Cell(up,start.y,neighbour_cell)
        if target_cell.v <= (start_cell.v + 1):
            if str(target_cell) not in visited:
                valid_directions.append(target_cell)
    down = start.x + 1
    if not down >= len(matrix):
        neighbour_cell = matrix[down][start.y]  
        neighbour_cell = translate_start_and_end_cells(neighbour_cell)
        target_cell: Cell = Cell(down,start.y,neighbour_cell)
        if target_cell.v <= (start_cell.v + 1):
            if str(target_cell) not in visited:
                valid_directions.append(target_cell)
    left = start.y - 1
    if not left < 0:
        neighbour_cell = matrix[start.x][left]  
        neighbour_cell = translate_start_and_end_cells(neighbour_cell)
        target_cell: Cell = Cell(start.x,left,neighbour_cell)
        if target_cell.v <= (start_cell.v + 1):
            if str(target_cell) not in visited:
                valid_directions.append(target_cell)
    right = start.y + 1
    if not right >= len(matrix[0]):
        neighbour_cell = matrix[start.x][right]  
        neighbour_cell = translate_start_and_end_cells(neighbour_cell)
        target_cell: Cell = Cell(start.x,right,neighbour_cell)
        if target_cell.v <= (start_cell.v + 1):
            if str(target_cell) not in visited:
                valid_directions.append(target_cell)
    return valid_directions


if __name__ == "__main__":
   # main('sample_input')
   main('input')
