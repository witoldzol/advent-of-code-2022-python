def main(file: str):
    # up = x - 1
    # down = x + 1
    # left = y - 1
    # right = y + 1
    # postion [x,y]
    matrix = []
    head_position = {'x':0, 'y':0}
    tail_position = {'x':0, 'y':0}
    with open(file, 'r') as f:
        t = 0 
        for line in f:
            if t == 5:
                break
            t += 1
            direction, times = line.split(' ')
            print(direction, times)

            for _ in range(int(times)):
                match direction:
                    case 'L':
                        print('goint left')
                        head_position['y'] -= 1
                        if is_tail_too_far_behind(head_position, tail_position):
                            print(f'head is {head_position["x"], head_position["y"]}')
                            print(f'tail is {tail_position["x"], tail_position["y"]}')
                            print('moving tail to head')
                    case 'R':
                        print('oing right')
                        head_position['y'] += 1
                        if is_tail_too_far_behind(head_position, tail_position):
                            print(f'head is {head_position["x"], head_position["y"]}')
                            print(f'tail is {tail_position["x"], tail_position["y"]}')
                            print('moving tail to head')
                    case 'D':
                        print('oing down')
                        head_position['x'] += 1
                        if is_tail_too_far_behind(head_position, tail_position):
                            print(f'head is {head_position["x"], head_position["y"]}')
                            print(f'tail is {tail_position["x"], tail_position["y"]}')
                            print('moving tail to head')
                    case 'U':
                        print('going up')
                        head_position['x'] -= 1
                        if is_tail_too_far_behind(head_position, tail_position):
                            print(f'head is {head_position["x"], head_position["y"]}')
                            print(f'tail is {tail_position["x"], tail_position["y"]}')
                            print('moving tail to head')
                    case _:
                        raise Exception('unknown command')

            print(head_position)

def is_tail_too_far_behind(head_position: dict, tail_position: dict) -> bool:
    return abs(head_position['x'] - tail_position['x']) > 1 or \
           abs(head_position['y'] - tail_position['y']) > 1
# 1 1 1
# T 1 H
# 1 1 1
  # tail 1,0
  # head 1,1



if __name__ == '__main__':
    main('input')
