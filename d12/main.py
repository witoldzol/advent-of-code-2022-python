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
    # lowest_cells = []
    lowest_cells: List[Cell] = find_lowest_cells(matrix)
    start = find_start(matrix)
    print('start cell ', start)
    start_cell = Cell(start[0], start[1], "a")
    lowest_cells.append(start_cell)
    min = 999999999
    for i, start_cell in enumerate(lowest_cells):
        # print(f"START traversal with start at {start_cell}")
        print(f"there are {len(lowest_cells) - i } starts left to traverse")
        path = breadth_traverse(matrix, start_cell, min)
        if path:
            print(path)
        if start_cell.x == 20 and start_cell.y == 0:
            print("##################################################################")
            print("##################################################################")
            print("##################################################################")
            print("##################################################################")
            print('bob')
            print(start_cell)
            print("##################################################################")
            print("##################################################################")
            print("##################################################################")
            print("##################################################################")
            print("##################################################################")
        if path and (len(path) < min):
            # print('path is ', path)
            print("========================================================")
            print('settign new min ', len(path))
            print("========================================================")
            min = len(path)
    print(f"minimum steps is => {min}")
    visualise_path(len(matrix), len(matrix[0]), path)


def find_lowest_cells(matrix: List[List[str]]):
    low_cells = []
    for x, row in enumerate(matrix):
        for y, cell in enumerate(row):
            if cell == "a":
                low_cells.append(Cell(x, y, "a"))
    return low_cells


def find_start(matrix: List[List[str]]) -> Tuple[int, int]:
    for x, row in enumerate(matrix):
        for y, cell in enumerate(row):
            if cell == "S":
                return x, y
    return 0, 0


def visualise_path(x: int, y: int, path: List[str]) -> None:
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
        print(f"Found ending at {d.x},{d.y}")
        return True


def breadth_traverse(matrix: List[List[str]], start_cell: Cell, min: int) -> List[str]:
    path: List[str] = []
    count = 0
    visited: Dict[str, bool] = {}
    next_to_visit: Queue = Queue()
    valid_directions: List[Cell] = get_valid_directions(matrix, visited, start_cell)
    reached_end: bool = False
    # init queue
    for d in valid_directions:
        next_to_visit.put(d)
    parent_map = {}
    for cell in iter(next_to_visit.get, None):
        #print('here we go cell = ', cell)
        count += 1
        if count > min:
            print("count is higher than min, skipping this traversal")
            return []
        if str(cell) in visited:
            # print('eize of queue ', )
            # print('oh noe we been here before')
            if next_to_visit.qsize() == 0:
                return []
            continue
        visited[str(cell)] = True
        print(f'visited {cell}')
        valid_directions: List[Cell] = get_valid_directions(matrix, visited, cell)
        # print(f'valid directions = {valid_directions}')
        # print(f'size of queue is = {next_to_visit.qsize()}')
        # check if end found
        if next_to_visit.qsize() == 0 and reached_end == False and not valid_directions:
            print('DEAD END, bailing out')
            return []
        for child in valid_directions:
            if is_end(matrix, child):
                print('FOUND END')
                reached_end = True
                parent_map[str(child)] = str(cell)
                path = trace_back_path(child, parent_map)
                return path
            if str(child) not in visited:
                parent_map[str(child)] = str(cell)
                next_to_visit.put(child)
    print('returning path', path)
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
    main('sample_input')
    # main("input")
