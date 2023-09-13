from typing import List


def main():
    with open("sample_input", "r") as f:
        forest = []
        for l in f:
            s = list(l.rstrip())
            forest.append(s)

def is_edge_tree(x: int):
    return x-1 < 0

def count_visible_trees(forest: List[List[int]]) -> int:
    count = 0
    for x, row in enumerate(forest):
        for y, tree in enumerate(row):
            # top
            if is_edge_tree(x):
                count += 1
                continue
            tree_above = forest[x-1][y]
            if tree_above > tree:
                print(f'tree {tree} [{x},{y}] is obscured by tree above {tree_above}')
                continue
            count += 1
    return count


if __name__ == "__main__":
    main()
