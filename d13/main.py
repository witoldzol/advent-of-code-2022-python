from typing import List
import re
from re import Match
from dataclasses import dataclass


@dataclass
class Token:
    parent: "Token"
    val: List


def main(filename):
    index = 0
    result = 0
    with open(filename, "r") as f:
        packets = []
        for line in f:
            line = line.rstrip()
            # print('===========')
            # print(line)
            # print('===========')
            if is_empty_line(line):
                continue
            packets.append(line)
            if len(packets) == 2:
                index += 1
                x, y = packets
                first_packet = parse_packet(x)
                second_packet = parse_packet(y)
                explore(first_packet, second_packet)
                if explore(first_packet, second_packet):
                    result += index
                packets = []
    print(f"Sum of indices is {result}")


def explore(left: int | List, right: int | List, n:int = 0, modified = False):
    print(f'EXPLORE CALL NUMBER {n}')
    n+=1
    print(f"[START]  LEFT = {left} and RIGHT = {right}")
    if not left and not right:
        print('left and right are empty or null')
        print(f"===> RETURNING TRUE for left = {left} and right = {right}")
        return True
    if left and not right:
        if modified:
            print('returning true because right ran out of items, and INT was modified to a LIST"t')
            print(f"===> RETURNING FALSE for left = {left} and right = {right}")
            return True
        print('returning true because left has items and right doesn"t')
        print(f"===> RETURNING FALSE, left has items, right is out.")
        return False
    if not left and right:
        print('returning true because left has no items and right does ')
        print(f"===> RETURNING TRUE for left = {left} and right = {right}")
        return True
    # BASE
    if isinstance(left, int) and isinstance(right, int):
        print(f"this is the base, is {left } >= {right} ? ", left >= right)
        return left <= right
    # LEFT
    if not left:
        l = None
        lr = None
    elif isinstance(left, list):
        l = left[0]
        lr = left[1:]
        if not lr:
            lr = None
    else: # left is int
        if isinstance(right,list):
            print(f'left is and int {left}, and right {right} is a list, upgrading left to a list')
            # l = [left]
            l = left
            modified = True
        else:
            l = left
        lr = None
    # RIGHT
    if not right:
        r = None
        rr = None
    elif isinstance(right, list):
        r = right[0]
        rr = right[1:]
        if not rr:
            rr = None
    else: # right is int
        if isinstance(left,list):
            print(f'right is and int {right}, and left {left} is a list, upgrading right to a list')
            # r = [right]
            r = right
            modified = True
        else:
            r = right
        rr = None
    print(f"L => {left}\nR => {right}\nleft reminder = {lr}\nright reminder = {rr}\n")
    if not lr and not rr:
        print('there is no reminder, returning simple comparison')
        return explore(l, r,n, modified)
    else:
        return explore(l, r,n, modified) and explore(lr, rr,n, modified)


def compare(left: List, right: List, mixed: bool = False) -> bool:
    print(f"STARTING comparison of left = {left} and righ = {right}")
    if not left and not right:
        return True
    for i, l in enumerate(left):
        print("iteration: ", i)
        if i >= len(right):
            print("[INFO] right side ran out of items")
            if mixed:
                return True
            return False
        r = right[i]
        if isinstance(l, list) and isinstance(r, list):
            print("Two lists detected, iterating over")
            if not compare(l[:1], r[:1], mixed):
                return False
        elif type(l) != type(r):
            print(f"types dont match left is {type(l)} and right is {type(r)}")
            if type(l) == list:
                return compare(l, [r], True)
            return compare([l], r, True)
        if l > r:
            return False
    return True


def is_empty_line(line: str) -> Match[str] | None:
    return re.match(r"^$", line)


def parse_packet(packet: str) -> List[Token]:
    if not packet:
        return []
    parent: Token = None
    for c in packet:
        match c:
            case "[":
                t = Token(parent, [])
                parent = t
            case "]":
                temp = parent
                if parent.parent:  # if we get back to root, do nothing
                    parent = parent.parent
                    parent.val.append(temp.val)
            case "0":
                parent.val.append(int(c))
            case "1":
                parent.val.append(int(c))
            case "2":
                parent.val.append(int(c))
            case "3":
                parent.val.append(int(c))
            case "4":
                parent.val.append(int(c))
            case "5":
                parent.val.append(int(c))
            case "6":
                parent.val.append(int(c))
            case "7":
                parent.val.append(int(c))
            case "8":
                parent.val.append(int(c))
            case "9":
                parent.val.append(int(c))
            case ",":
                continue
            case _:
                raise Exception(f"Unknown input {c}")
    return parent.val


if __name__ == "__main__":
    main("sample_input")
    # main("input") #440 last try
