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
            if t == 7: #
                break #
            t += 1 # todo - reomve
            direction, times = line.split(' ')
            print(direction, times)

            for _ in range(int(times)):
                match direction:
                    case 'L':
                        print('goint left')
                        head_position['y'] -= 1
                        print(f'current head positon = {head_position}')
                        if is_tail_too_far_behind(head_position, tail_position):
                            move_tail_to_head(head_position, tail_position)
                    case 'R':
                        print('oing right')
                        head_position['y'] += 1
                        print(f'current head positon = {head_position}')
                        if is_tail_too_far_behind(head_position, tail_position):
                            move_tail_to_head(head_position, tail_position)
                    case 'D':
                        print('oing down')
                        head_position['x'] += 1
                        print(f'current head positon = {head_position}')
                        if is_tail_too_far_behind(head_position, tail_position):
                            move_tail_to_head(head_position, tail_position)
                    case 'U':
                        print('going up')
                        head_position['x'] -= 1
                        print(f'current head positon = {head_position}')
                        if is_tail_too_far_behind(head_position, tail_position):
                            move_tail_to_head(head_position, tail_position)
                    case _:
                        raise Exception('unknown command')

            print(head_position)


def move_tail_to_head(head_position: dict, tail_position: dict):
    print(f'head is {head_position["x"], head_position["y"]}')
    print(f'tail is {tail_position["x"], tail_position["y"]}')
    dx = head_position['x'] - tail_position['x']
    dy = head_position['y'] - tail_position['y']
    if is_head_diagonal_to_tail(head_position, tail_position):
        print('head is DIAGONAL to tail')
        if dx > 1:
            dx = 1
        if dx < -1:
            dx = -1
        if dy > 1:
            dy = 1
        if dy < -1:
            dy = -1
        print(f'moving tails diagonally {dx},{dy}')
    else:
        if dx == 0:
            if dy > 0:
                dy -= 1
            else:
                dy += 1
        else:
            if dx > 0:
                dx -= 1
            else:
                dx += 1
        print(f'moving tail by {dx},{dy}')
    tail_position['x'] += dx
    tail_position['y'] += dy
    print(f'current tail position is {tail_position}')


def is_tail_too_far_behind(head_position: dict, tail_position: dict) -> bool:
    return abs(head_position['x'] - tail_position['x']) > 1 or \
           abs(head_position['y'] - tail_position['y']) > 1

def is_head_diagonal_to_tail(head_position: dict, tail_position: dict) -> bool:
    return head_position['x'] != tail_position['x'] and \
           head_position['y'] != tail_position['y']


# NORMAL move
# (0,2) (2,2)
# head(x) - tail(x) = -2x -> x - 1 # the sign doesn't change
#-> go up (x-1, y+1)
# 1 1 H 1
# 1 1 1 1
# 1 1 T 1
# 1 1 1 1

#-> go down 
# (3,2) (1,2)
# head(x) - tail(x) = 2x => x + 1 # the sign doesn't change
# 1 1 1 1
# 1 1 T 1
# 1 1 1 1
# 1 1 H 1


#-> go left
# (1,1) (1,3)
# head(y) - tail(y) = -2y => y - 1 # the sign doesn't change
# 1 1 1 1
# 1 H 1 T
# 1 1 1 1
# 1 1 1 1


#-> go right 
# h(0,3) (0,1)
# head(y) - tail(y) = 2y => y + 1 # the sign doesn't change
# 1 T 1 H
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1

# DIAGONAL
#-> go up + right (x-1, y+1)
# h(0,2) t(2,1) h-t=-2,1
# we want to go one up(x), one right(y)
# 1 1 H 1
# 1 1 1 1
# 1 T 1 1
# 1 1 1 1

#-> go down + right (x+1, y+1)
# h(3,2) t(1,1) h-t 2,1
# we want to go one down(x) and one right(y)
# 1 1 1 1
# 1 T 1 1
# 1 1 1 1
# 1 1 H 1
# diagonal case

#-> go down + left (x+1, y-1)
# h(3,2) t(1,3) h-t 2,-1
# tail goes one down(x) and one left(y)
# 1 1 1 1
# 1 1 1 T
# 1 1 1 1
# 1 1 H 1
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
