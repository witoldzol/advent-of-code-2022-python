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
            print('times`', times)
            for _ in range(int(times)):
                print(f'moving in direction of {direction}')

if __name__ == '__main__':
    main('input')
