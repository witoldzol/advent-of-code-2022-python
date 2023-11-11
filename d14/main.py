import sys
from typing import List, Tuple
import argparse
import logging as log

SAND_ENTRY_POINT = 500


parser = argparse.ArgumentParser()
parser.add_argument("-log")
log_level = parser.parse_args().log
log.basicConfig(level=log_level)


def main(filename):
    coords = parse_coords(filename)
    cave, entry_coordinates = draw_cave(coords)
    i = 0
    while move_sand(cave, entry_coordinates) == 0:
        i += 1
    log.warn(f"Total number of sand pieces that came to rest = {i}")
    print_cave(cave)


def print_cave(cave) -> None:
    with open("cave", "w") as f:
        for row in cave[490:]:
            f.write(" ".join(row))
            f.write("\n")


def move_sand(cave: List[List[str]], sand_coords: Tuple[int, int]) -> int:
    x, y = sand_coords
    i = 1
    max_drop = 1000
    current_drop = 0
    # check if entrypoint is free
    if cave[x][y + i] != ".":
        log.error("Entrypoint is blocked, no more sand can go through")
        return -1
    while True:
        try:
            # go down?
            if cave[x][y + i] == ".":
                log.info(f"Moving `down`, {x},{y+i}")
                i += 1
                current_drop += 1
                if current_drop > max_drop:
                    log.info("We found the abbys, ending program")
                    return 1
            # go left?
            elif cave[x - 1][y + i] == ".":
                log.info(f"Moving `left`, {x},{y+i}")
                x -= 1
                continue
            elif cave[x + 1][y + i] == ".":
                log.info(f"Moving `right`, {x},{y+i}")
                x += 1
                continue
            else:
                log.info(
                    f"Cant move any further, sand coming to rest at location {x},{y+i-1}"
                )
                cave[x][y + i - 1] = "o"
                break
        except IndexError as e:
            log.info("We found the abbys, ending program")
            return 1
    return 0


def parse_coords(filename: str) -> List[List[List[int]]]:
    with open(filename, "r") as input:
        result = []
        for line in input:
            temp = []
            coords = line.strip().split("->")
            for c in coords:
                out = [int(x) for x in c.split(",")]
                temp.append(out)
            result.append(temp)
    print(result)
    return result


def draw_cave(coords: List[List[List[int]]]) -> List[List[str]]:
    # draw empty cave
    min_x, max_x, min_y, max_y = get_min_max_x_y(coords)
    cave = [[] for _ in range(min_x, max_x + 1)]
    for x in cave:
        for _ in range(min_y, max_y + 1):
            x.append(".")
    # draw rocks
    for c in coords:
        for i in range(len(c) - 1):
            log.debug(f"Raw coords = {c}")
            start_x, start_y = c[i]
            end_x, end_y = c[i + 1]
            log.debug(f"Drawing {start_x},{start_y} ->{end_x},{end_y}")
            start_x = start_x - min_x
            start_y = start_y - min_y
            end_x = end_x - min_x
            end_y = end_y - min_y
            log.debug("start x ", start_x, "end x ", end_x)
            log.debug("start y ", start_y, "end y ", end_y)
            if start_x > end_x:
                start_x, end_x = swap(start_x, end_x)
            if start_y > end_y:
                start_y, end_y = swap(start_y, end_y)
            if start_x - end_x == 0:
                for i in range(start_y, end_y + 1):
                    cave[start_x][i] = "#"
            else:
                pass
                for i in range(start_x, end_x + 1):
                    cave[i][start_y] = "#"
    cave[SAND_ENTRY_POINT][0] = "+"
    return cave, (SAND_ENTRY_POINT, 0)


def get_min_max_x_y(coords: List[List[List[int]]]) -> Tuple[int, int, int, int]:
    min_x = 0
    min_y = 0
    max_x = -1
    max_y = -1
    for c in coords:
        for x, y in c:
            if x > max_x:
                max_x = x
            elif y > max_y:
                max_y = y
    print(f"[LOG] min_x = {min_x}, min_y = {min_y}, max_x = {max_x}, max_y = {max_y}")
    return min_x, max_x, min_y, max_y


def swap(x, y):
    temp = x
    x = y
    y = temp
    return x, y


if __name__ == "__main__":
    # main("sample_input")
    main("input")
