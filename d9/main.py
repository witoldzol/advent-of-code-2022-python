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
        t = 0  # todo remove
        for line in f:  
            if t == 5: #
                break #
            t += 1 # todo - reomve
            direction, times = line.split(' ')
            print(direction, times)

            for _ in range(int(times)):
                match direction:
                    case 'L':
                        print('goint left')
                        head_position['y'] -= 1
                        if is_tail_too_far_behind(head_position, tail_position):
                            if is_head_diagonal_to_tail(head_position, tail_position):
                                print('head is diagonal to tail')
                            print(f'head is {head_position["x"], head_position["y"]}')
                            print(f'tail is {tail_position["x"], tail_position["y"]}')
                            move_tail_to_head(head_position, tail_position)
                    case 'R':
                        print('oing right')
                        head_position['y'] += 1
                        if is_tail_too_far_behind(head_position, tail_position):
                            if is_head_diagonal_to_tail(head_position, tail_position):
                                print('head is diagonal to tail')
                            print(f'head is {head_position["x"], head_position["y"]}')
                            print(f'tail is {tail_position["x"], tail_position["y"]}')
                            move_tail_to_head(head_position, tail_position)
                    case 'D':
                        print('oing down')
                        head_position['x'] += 1
                        if is_tail_too_far_behind(head_position, tail_position):
                            if is_head_diagonal_to_tail(head_position, tail_position):
                                print('head is diagonal to tail')
                            print(f'head is {head_position["x"], head_position["y"]}')
                            print(f'tail is {tail_position["x"], tail_position["y"]}')
                            move_tail_to_head(head_position, tail_position)
                    case 'U':
                        print('going up')
                        head_position['x'] -= 1
                        if is_tail_too_far_behind(head_position, tail_position):
                            if is_head_diagonal_to_tail(head_position, tail_position):
                                print('head is diagonal to tail')
                            print(f'head is {head_position["x"], head_position["y"]}')
                            print(f'tail is {tail_position["x"], tail_position["y"]}')
                            move_tail_to_head(head_position, tail_position)
                    case _:
                        raise Exception('unknown command')

            print(head_position)


def move_tail_to_head(head_position: dict, tail_position: dict):
    print('moving tail to head')


def is_tail_too_far_behind(head_position: dict, tail_position: dict) -> bool:
    return abs(head_position['x'] - tail_position['x']) > 1 or \
           abs(head_position['y'] - tail_position['y']) > 1

def is_head_diagonal_to_tail(head_position: dict, tail_position: dict) -> bool:
    return head_position['x'] != tail_position['x'] and \
           head_position['y'] != tail_position['y']

# 1 H 1 1
# 1 1 1 1
# 1 T 1 1
# 1 1 1 1

#0,1 - 2,1 ( diff(x) > 1 ) - we move on x axis 
#(if diff is negative, we move 'up', ie, decrease x value of tail)
# in this case, we know its not diagonal because y axis matches up ( H & T are on the same axis)

#-> go up + right (x-1, y+1)
# 1 1 H 1
# 1 1 1 1
# 1 T 1 1
# 1 1 1 1

#-> go down + right (x+1, y+1)
# 1 1 1 1
# 1 T 1 1
# 1 1 1 1
# 1 1 H 1
# diagonal case

#-> go down + left (x+1, y-1)
# 1 1 1 1
# 1 1 1 T
# 1 1 1 1
# 1 H 1 1
# diagonal case

#-> go up + left (x-1, y-1)
# 1 H 1 1
# 1 1 1 T
# 1 1 1 1
# 1 1 1 1
# diagonal case

# head 0,2
# tail 2,1
# we have to inc/decrement both x & y values of tail
# how do we detect diagonal ? neither x && y are not aligned
# eg. x index & y index do not match up at all ( H & T are not on the same axis )



if __name__ == '__main__':
    main('input')
