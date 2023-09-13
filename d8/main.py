from typing import List


def main(file):
    forest = []
    with open(file, "r") as f:
        for l in f:
            s = list(l.rstrip())
            forest.append(s)

    return count_visible_trees(forest)

def is_edge_tree(x: int, y: int , lx: int, ly: int):
    return x == 0 or \
           y == 0 or \
           x+1 >= lx or \
           y+1 >= ly

def count_visible_trees(forest: List[List[int]]) -> int:
    count = 0
    for x, row in enumerate(forest):
        for y, tree in enumerate(row):
            # top
            if is_edge_tree(x, y, len(forest), len(forest[0])):
                count += 1
                continue
            tree_above = forest[x-1][y]
            tree_below = forest[x+1][y]
            tree_left = forest[x][y-1]
            tree_right = forest[x][y+1]
            if tree_above >= tree and tree_below >= tree and tree_left >= tree and tree_right >= tree:
                print(f'tree {tree} [{x},{y}] is obscured by tree above {tree_above} \n \
                      and below {tree_below} \n \
                      and to the left {tree_left} \n \
                      and to the right {tree_right}')
                continue
            count += 1
    return count


if __name__ == "__main__":
    main('sample_input')
