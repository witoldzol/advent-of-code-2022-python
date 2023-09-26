from typing import List, Dict, Tuple
from queue import Queue


class Cell:
    x: int
    y: int
    v: int

    def __init__(self, x: int, y: int, v: str):
        self.x = x
        self.y = y
        self.v = ord(v)

    def __str__(self) -> str:
        return f"{self.x},{self.y}"

    def __repr__(self) -> str:
        return f"Cell(x={self.x},y={self.y},v={self.v})"


def main(filename):
    matrix = build_matrix(filename)
    lowest_cells: List[Cell] = find_lowest_cells(matrix)
    min = 999999999
    shortest_path = []
    for i, start_cell in enumerate(lowest_cells):
        print(f"There are {len(lowest_cells) - i } starts left to traverse")
        path = breadth_traverse(matrix, start_cell, min)
        if path and (len(path) < min):
            min = len(path)
            shortest_path = path
    visualise_path(len(matrix), len(matrix[0]), shortest_path)
    print(f'The minimum amount of steps is {min}')

def find_lowest_cells(matrix: List[List[str]]) -> List[Cell]:
    low_cells = []
    for x, row in enumerate(matrix):
        for y, cell in enumerate(row):
            if cell == "a" or cell == 'S':
                low_cells.append(Cell(x, y, "a"))
    return low_cells


def find_start(matrix: List[List[str]]) -> Tuple[int, int]:
    for x, row in enumerate(matrix):
        for y, cell in enumerate(row):
            if cell == "S":
                return x, y
    return 0, 0


def visualise_path(x: int, y: int, path: List[str]) -> None:
    if not path:
        return
    matrix = []
    for _ in range(x):
        temp = []
        for _ in range(y):
            temp.append(".")
        matrix.append(temp)
    for cell in path:
        x, y = cell.split(",")
        matrix[int(x)][int(y)] = "="
    for row in matrix:
        r = "".join(row)
        print(r)


def build_matrix(filename: str) -> List[List[str]]:
    matrix = []
    with open(filename, "r") as f:
        for line in f:
            line = line.rstrip()
            matrix.append(list(line))
    return matrix


def is_end(matrix, d):
    if matrix[d.x][d.y] == "E":
        return True


def breadth_traverse(matrix: List[List[str]], start_cell: Cell, min: int) -> List[str]:
    path: List[str] = []
    visited: Dict[str, bool] = {}
    next_to_visit: Queue = Queue()
    valid_directions: List[Cell] = get_valid_directions(matrix, visited, start_cell)
    reached_end: bool = False
    # init queue
    for d in valid_directions:
        next_to_visit.put(d)
    parent_map = {}
    for cell in iter(next_to_visit.get, None):
        if str(cell) in visited:
            if next_to_visit.qsize() == 0:
                return []
            continue
        visited[str(cell)] = True
        valid_directions: List[Cell] = get_valid_directions(matrix, visited, cell)
        if next_to_visit.qsize() == 0 and reached_end == False and not valid_directions:
            return []
        for child in valid_directions:
            if is_end(matrix, child):
                reached_end = True
                parent_map[str(child)] = str(cell)
                path = trace_back_path(child, parent_map)
                return path
            if str(child) not in visited:
                parent_map[str(child)] = str(cell)
                next_to_visit.put(child)
    return path


def trace_back_path(end: Cell, map: Dict[str, str]) -> List[str]:
    path = []
    path.append(str(end))
    current = str(end)
    while current in map:
        parent: str = map[current]
        path.append(parent)
        current = parent
    return path


def translate_start_and_end_cells(cell: str) -> str:
    match cell:
        case "E":
            return "z"
        case "S":
            return "|"  # | is the 2 chars after z, and will always be 'higher than start cell ( hence S will never be valid direction)
    return cell


def is_out_of_bounds(offset: List[int], len_x: int, len_y: int) -> bool:
    if offset[0] < 0 or offset[1] < 0:
        return True
    if offset[0] >= len_x or offset[1] >= len_y:
        return True
    return False


def get_valid_directions(
    matrix: List[List[str]], visited: Dict[str, bool], start: Cell
) -> List[Cell]:
    valid_directions: List[Cell] = []
    offsets = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for x, y in offsets:
        offset = [start.x + x, start.y + y]
        if is_out_of_bounds(offset, len(matrix), len(matrix[0])):
            continue
        cell_value = matrix[offset[0]][offset[1]]
        cell_value = translate_start_and_end_cells(cell_value)
        target_cell: Cell = Cell(offset[0], offset[1], cell_value)
        if target_cell.v <= (start.v + 1):
            if str(target_cell) not in visited:
                valid_directions.append(target_cell)
    return valid_directions


if __name__ == "__main__":
    # main('sample_input')
    main("input")
