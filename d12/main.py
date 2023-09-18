from typing import List


def main(filename):
    # check all adjecent cells
    # loop over valid ones 
    # each call will be recursive
    # pass location from where you came, to avoid backtracking
    start = [0,0]
    end = [2,5]
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


def traverse(matrix: List[List[str]], start: List[int], end: List[int]) -> int:
    return 31

if __name__ == "__main__":
    main('sample_input')
