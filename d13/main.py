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
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print(f'START NEW EXPLORATION >>>>>>>>>>>>>>>>>>')
                print(f"[START]  LEFT = {first_packet} and RIGHT = {second_packet}")
                if explore(first_packet, second_packet):
                    result += index
                    print('RESULT -------> IN ORDER')
                    print(f'Current Index {index}, current result {result}')
                else:
                    print('RESULT -------> OUT OF ORDER')
                print(f'END OF EXPLORATION <<<<<<<<<<<<<<<<<<<<<')
                print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                print('')
                packets = []
    print(f"Sum of indices is {result}")


def explore(left:  List, right: List):
    if not left and right:
        print(f"[ RIGHT ran out of items ]  LEFT = {left} and RIGHT = {right}")
        return True
    if left and not right:
        print(f"[ LEFT ran out of items ]  LEFT = {left} and RIGHT = {right}")
        return False
    while left and right:
        l = left[0]
        r = right[0]
        left = left[1:]
        right = right[1:]
        print(f'comparing left { left } to right { right }')
        result = compare(l,r)
        if result != None:
            return result
        if not left and right:
            print(f"[ RIGHT ran out of items ]  LEFT = {left} and RIGHT = {right}")
            return True
        if left and not right:
            print(f"[ LEFT ran out of items ]  LEFT = {left} and RIGHT = {right}")
            return False
    print(f"[ RETURNING TRUE as default ]  LEFT = {left} and RIGHT = {right}")
    return True

def compare2(p1: int|List, p2):
    # both are ints
    if isinstance(p1, int) and isinstance(p2, int):
        if p1 > p2:
            return False 
        elif p2 > p1:
            return True
        else:
            return None
    # both are lists
    # if isinstance(p1, list) and isinstance(p2, list):
    #     i = 0
    #     while i<len(p1) and i<len(p2):
    # one is int other is list

def compare(left: int | List, right: int | List):
    print(f"[COMPARE]  LEFT = {left} and RIGHT = {right}")
    if not left and not right:
        print('=> RETURN NONE, left and right are empty or null')
        return None
    if left and not right:
        print(f"===> RETURN FALSE, left has items, right is out.")
        return False
    if not left and right:
        print('====> RETURN TRUE because left has no items and right does ')
        return True
    # BASE
    if isinstance(left, int) and isinstance(right, int):
        if left != right:
            print(f"BASE CONDITION, is {left } < {right} ? ", left < right)
            return left < right
        print("=> RETURN NONE, left and right are  the same")
        return None
    if isinstance(left, list) and isinstance(right, int):
        right = [right]
    elif isinstance(right, list) and isinstance(left, int):
        left = [left]
    l = left[0]
    lr = left[1:]
    if not lr:
        lr = None
    r = right[0]
    rr = right[1:]
    if not rr:
        rr = None
    print(f"GOING DEEPER\nL => {l}\nR => {r}\nleft reminder = {lr}\nright reminder = {rr}\n")
    r = compare(l,r)
    if r == None:
        return compare(lr,rr)
    else:
        return r # todo - not sure about this logic, do some testing


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
    # main("sample_input")
    main("input") #5867 last try
