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
    return 31

def build_matrix(filename: str) -> List['str']:
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            matrix.append(list(line))
    return matrix

if __name__ == "__main__":
    main('sample_input')
