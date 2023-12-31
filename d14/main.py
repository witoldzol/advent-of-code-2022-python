from typing import List, Tuple
import argparse
import logging as log

SAND_ENTRY_POINT = 500
CAVE_EXTENSION_OFFSET = 1100


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
    # we add one, because we didn't count the last piece of sand that blocked the entrance
    log.warn(f"Total number of sand pieces that came to rest = {i + 1}")
    # print_cave(cave)
    save_cave(cave)


def print_cave(cave) -> None:
    for row in cave[490:]:
        log.info(row)


def save_cave(cave) -> None:
    with open("cave", "w") as f:
        for row in cave[490:]:
            f.write("".join(row))
            f.write("\n")


def move_sand(cave: List[List[str]], sand_coords: Tuple[int, int]) -> int:
    x, y = sand_coords
    i = 1
    # check if entrypoint is free
    if (
        cave[x][y + i] != "."
        and cave[x - 1][y + i] != "."
        and cave[x + 1][y + 1] != "."
    ):
        log.error("Entrypoint is blocked directly below, left and right!")
        return -1
    while True:
        try:
            # go down?
            if cave[x][y + i] == ".":
                log.info(f"Moving `down`, {x},{y+i}")
                i += 1
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


def draw_cave(coords: List[List[List[int]]]) -> Tuple[List[List[str]], Tuple[int, int]]:
    min_x, max_x, min_y, max_y = get_min_max_x_y(coords)
    min_x -= CAVE_EXTENSION_OFFSET
    max_x += CAVE_EXTENSION_OFFSET
    cave = [[] for _ in range(min_x, max_x + 1)]
    # draw empty cave
    for x in cave:
        for _ in range(min_y, max_y + 1 + CAVE_EXTENSION_OFFSET):
            x.append(".")
    # draw rocks
    for c in coords:
        # -1 because we have a moving window, that grabs 1,2; 2,3; 3;4 ...
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
                for i in range(start_x, end_x + 1):
                    cave[i][start_y] = "#"
    # draw the floor, max + offset
    for x in range(min_x, max_x + 1):
        cave[x][max_y + 2] = "#"

    cave[SAND_ENTRY_POINT + CAVE_EXTENSION_OFFSET][
        0
    ] = "+"  # add two because we widened the cave by 2 place
    return cave, (SAND_ENTRY_POINT + CAVE_EXTENSION_OFFSET, 0)


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
    main("input")  # 1135 -> too low
