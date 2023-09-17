def main(file):
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
                    cycle, signal_strenght, x = increment_signal(cycle, signal_strenght, x)
                case 'addx':
                    cycle, signal_strenght, x = increment_signal(cycle, signal_strenght, x)
                    cycle, signal_strenght, x = increment_signal(cycle, signal_strenght, x)
                    x += val

    print(f'The sum of signal strenght is {signal_strenght}')


def increment_signal(cycle: int, signal_strenght: int, x: int):
    STEPS = [20, 60, 100, 140, 180, 220]
    cycle += 1
    for step in STEPS:
        if cycle == step:
            signal_strenght += cycle * x
    return cycle, signal_strenght, x


if __name__ == '__main__':
    main('sample_input')
