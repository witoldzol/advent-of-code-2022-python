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
            if is_empty_line(line):
                continue
            packets.append(line)
            if len(packets) == 2:
                index += 1
                x, y = packets
                first_packet = parse_packet(x)
                second_packet = parse_packet(y)
                print(f'START NEW EXPLORATION ==================')
                explore(first_packet, second_packet)
                print(f'END OF EXPLORATION <<<<<<<<<<<<<<<<<<<<<')
                if explore(first_packet, second_packet):
                    result += index
                    print(f'Current Index {index}, current result {result}')
                packets = []
    print(f"Sum of indices is {result}")


def explore(left: int | List, right: int | List, n:int = 0):
    print(f'explore call number {n}')
    print(f"[START]  LEFT = {left} and RIGHT = {right}")
    n+=1
    if not left and not right:
        print('left and right are empty or null')
        print(f"===> RETURNING TRUE for left = {left} and right = {right}")
        return True
    if left and not right:
        print(f"===> RETURNING FALSE, left has items, right is out.")
        return False
    if not left and right:
        print('====> returning TRUE because left has no items and right does ')
        return True
    # BASE
    if isinstance(left, int) and isinstance(right, int):
        print(f"this is the base, is {left } <= {right} ? ", left <= right)
        if left == right:
            return left < right
        return None
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
        r = right
        rr = None
    if not lr and not rr:
        print('there is no reminder, returning simple comparison')
        return explore(l, r,n)
    else:
        print('going deeper, with reminder')
        print(f"L => {l}\nR => {r}\nleft reminder = {lr}\nright reminder = {rr}\n")
        return explore(l, r,n) or explore(lr, rr,n)


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
