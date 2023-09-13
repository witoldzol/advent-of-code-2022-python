from typing import List


def main():
    with open("sample_input", "r") as f:
        forest = []
        for l in f:
            s = list(l.rstrip())
            forest.append(s)
        # x_max = len(forest)
        # y_max = len(forest[0])
        # visible_trees_count = 0
        # for x, row in enumerate(forest):
        #     for y, tree in enumerate(row):
        #         pass


def count_visible_trees(forest: List[List[int]]) -> int:
    return 1


if __name__ == "__main__":
    main()
