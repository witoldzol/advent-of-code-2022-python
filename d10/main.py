from typing import List


def main(file):
    crt: List[List[str]] = []
    crt_line: List[str] = []
    signal_strenght = 0
    cycle = 0
    x = 1
    with open(file, 'r') as f:
        for line in f:
            command, *val = line.split(' ')
            if val:
                val = int(val[0].rstrip())
            match command.rstrip():
                case 'noop':
                    if len(crt_line) == 40:
                        print('cycyle ', cycle)
                        crt.append(crt_line)
                        crt_line = []
                    cycle, signal_strenght, x = increment_signal(cycle, signal_strenght, x)
                    crt_line = draw_to_crt(crt_line, cycle)
                case 'addx':
                    #1
                    if len(crt_line) == 40:
                        print('cycyle ', cycle)
                        crt.append(crt_line)
                        crt_line = []
                    cycle, signal_strenght, x = increment_signal(cycle, signal_strenght, x)
                    crt_line = draw_to_crt(crt_line, cycle)
                    #2
                    if len(crt_line) == 40:
                        print('cycyle ', cycle)
                        crt.append(crt_line)
                        crt_line = []
                    cycle, signal_strenght, x = increment_signal(cycle, signal_strenght, x)
                    crt_line = draw_to_crt(crt_line, cycle)
                    x += val
    crt.append(crt_line)
    print('final cycle is ', cycle)
    for crt_line in crt:
        print(crt_line)
    print(f'The sum of signal strenght is {signal_strenght}')


def increment_signal(cycle: int, signal_strenght: int, x: int):
    STEPS = [20, 60, 100, 140, 180, 220]
    cycle += 1
    for step in STEPS:
        if cycle == step:
            signal_strenght += cycle * x
    return cycle, signal_strenght, x

def draw_to_crt(crt: List[str], cycle: int):
    p = (cycle-1) % 40 
    crt.append(str(p))
    return crt


if __name__ == '__main__':
    main('sample_input')
