from typing import List


def main(file):
    forest = []
    with open(file, "r") as f:
        for l in f:
            s = list(l.rstrip())
            forest.append(s)
    count = count_visible_trees(forest)
    print(f'visible trees = {count}')
    return count 

def is_edge_tree(x: int, y: int , lx: int, ly: int):
    return x == 0 or \
           y == 0 or \
           x+1 >= lx or \
           y+1 >= ly

def is_higher_below(forest: List[List[int]], tree: int, x: int, y: int) -> int:
    count = 0
    for t in range(x+1, len(forest)):
        if forest[t][y] < tree:
            count += 1
        if forest[t][y] >= tree:
            count += 1
            break
    return count

def is_higher_above(forest: List[List[int]], tree: int, x: int, y: int) -> int:
    count = 0
    for t in range(x-1, -1, -1):
        if forest[t][y] < tree:
            count += 1
        if forest[t][y] >= tree:
            count += 1
            break
    return count

def is_higher_left(forest: List[List[int]], tree: int, x: int, y: int) -> int:
    count = 0
    for t in range(y-1, -1, -1):
        if forest[x][t] < tree:
            count += 1
        if forest[x][t] >= tree:
            count += 1
            break
    return count

def is_higher_right(forest: List[List[int]], tree: int, x: int, y: int) -> int:
    count = 0
    for t in range(y+1, len(forest)):
        if forest[x][t] < tree:
            count += 1
        if forest[x][t] >= tree:
            count += 1
            break
    return count

def count_visible_trees(forest: List[List[int]]) -> int:
    max = 0
    for x, row in enumerate(forest):
        for y, tree in enumerate(row):
            if is_edge_tree(x, y, len(forest), len(forest[0])):
                continue
            print('=======================')
            print(f' tree {x},{y} ')
            tree_above = is_higher_above(forest, tree, x , y)
            print(f'above = {tree_above}')
            tree_below = is_higher_below(forest, tree, x , y)
            print(f'below = {tree_below}')
            tree_left = is_higher_left(forest, tree, x , y) 
            print(f'left = {tree_left}')
            tree_right = is_higher_right(forest, tree, x , y) 
            print(f'right = {tree_right}')
            scenic_score =  tree_above * tree_below * tree_left * tree_right
            print('=======================')
            if scenic_score > max:
                max = scenic_score
    return max


if __name__ == "__main__":
    main('input')
