STEPS = [20, 60, 100, 140, 180, 220]
def main(file):
    counter = 0
    with open(file, 'r') as f:
        for line in f:
            command, *val = line.split(' ')
            match command:
                case 'noop':
                    counter += 1
                    for step in STEPS:
                        if counter % step == 0:
                            print(f'counter is at {counter}')
                case 'addx':
                    counter += 1
                    for step in STEPS:
                        if counter % step == 0:
                            print(f'counter is at {counter}')
                    counter += 1
                    for step in STEPS:
                        if counter % step == 0:
                            print(f'counter is at {counter}')
                    

if __name__ == '__main__':
    main('sample_input')
