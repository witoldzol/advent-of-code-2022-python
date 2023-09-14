def main(file: str):
    # up = x - 1
    # down = x + 1
    # left = y - 1
    # right = y + 1
    # postion [x,y]
    matrix = []
    head_position = [0,0]
    tail_position = [0,0]
    with open(file, 'r') as f:
        for line in f:
            direction, times = line.split(' ')
            print(direction, times)

            for _ in range(int(times)):
                match direction:
                    case 'L':
                        print('goint left')
                    case 'R':
                        print('oing right')
                    case 'D':
                        print('oing down')
                    case 'U':
                        print('going up')
                    case _:
                        raise Exception('unknown command')


if __name__ == '__main__':
    main('input')
