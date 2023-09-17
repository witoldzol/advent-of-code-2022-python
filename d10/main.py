from typing import List


def main(file):
    crt: List[List[str]] = []
    crt_line: List[str] = []
    signal_strenght = 0
    cycle = 0
    x = 1
    with open(file, "r") as f:
        for line in f:
            command, *val = line.split(" ")
            if val:
                val = int(val[0].rstrip())
            match command.rstrip():
                case "noop":
                    crt, crt_line = check_end_of_crt_line(crt, crt_line)
                    crt_line = draw_to_crt(crt_line, cycle, x)
                    cycle, signal_strenght, x = increment_signal( cycle, signal_strenght, x)
                case "addx":
                    # 1
                    crt, crt_line = check_end_of_crt_line(crt, crt_line)
                    crt_line = draw_to_crt(crt_line, cycle, x)
                    cycle, signal_strenght, x = increment_signal( cycle, signal_strenght, x)
                    # 2
                    crt, crt_line = check_end_of_crt_line(crt, crt_line)
                    crt_line = draw_to_crt(crt_line, cycle, x)
                    cycle, signal_strenght, x = increment_signal( cycle, signal_strenght, x)
                    x += val
    crt.append(crt_line)
    for crt_line in crt:
        print("".join(crt_line))
    print(f"The sum of signal strenght is {signal_strenght}")


def increment_signal(cycle: int, signal_strenght: int, x: int):
    STEPS = [20, 60, 100, 140, 180, 220]
    cycle += 1
    for step in STEPS:
        if cycle == step:
            signal_strenght += cycle * x
    return cycle, signal_strenght, x


def check_end_of_crt_line(crt, crt_line):
    if len(crt_line) == 40:
        crt.append(crt_line)
        crt_line = []
    return crt, crt_line


def draw_to_crt(crt: List[str], cycle: int, x: int):
    i = cycle % 40
    symbol = "."
    if i == x - 1 or i == x or i == x + 1:
        symbol = "#"
    crt.append(symbol)
    return crt


if __name__ == "__main__":
    main("input")
