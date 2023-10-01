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
                compare(first_packet, second_packet)
                if(compare2(first_packet, second_packet)):
                    result += index
                packets = []
    print(f"Sum of indices is {result}")


def explore(left: int|List, thresshold: int):
    print('exploring' , left)
    if not left:
        return False
    # base
    if isinstance(left, int):
        print(f'this is the base, is {left } >= {thresshold} ? ', left >= thresshold)
        return left >= thresshold
    l = left[0]
    print('exploring first ele in list ', l)
    reminder = left[1:]
    print('exploring reminder of the list', reminder)
    return explore(l, thresshold) or explore(reminder, thresshold)


def compare(left: List, right: List , mixed: bool = False) -> bool:
    print(f'STARTING comparison of left = {left} and righ = {right}')
    if not left and not right:
        return True

    for i, l in enumerate(left):
        print('iteration: ', i)
        if i >= len(right):
            print('[INFO] right side ran out of items')
            if mixed:
                return True
            return False
        r = right[i]
        if isinstance(l, list) and isinstance(r,list):
            print("Two lists detected, iterating over") # todo continue from heere
            if not compare(l[:1],r[:1],mixed):
                return False
        elif type(l) != type(r):
            print(f'types dont match left is {type(l)} and right is {type(r)}')
            if type(l) == list:
                return compare(l,[r], True)
            return compare([l], r, True)
        if l > r:
            return False
    return True

def compare2(left: List, right: List , mixed: bool = False) -> bool:
    if not left and not right:
        return True
    for i, l in enumerate(left):
        print('iteration: ', i)
        if i >= len(right):
            print('[INFO] right side ran out of items')
            if mixed:
                return True
            return False
        r = right[i]
        print('l = ', l)
        print('r = ', r)
        print(f'types are =>> left is {type(l)} and right is {type(r)}')
        if isinstance(l, list) and isinstance(r,list):
            print("Two lists detected, iterating over") # todo continue from heere
            return compare(l,r,mixed)
        elif type(l) != type(r):
            print(f'types dont match left is {type(l)} and right is {type(r)}')
            if type(l) == list:
                return compare(l,[r], True)
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
                if parent.parent: # if we get back to root, do nothing
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
    # main("sample_input")
    main("input")
