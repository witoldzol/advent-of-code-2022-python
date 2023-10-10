from typing import List
from dataclasses import dataclass


@dataclass
class Token:
    parent: "Token"
    val: List

def main(filename):
    with open(filename, 'r') as f:
        input = f.read().strip()
        result = 0
        for i, group in enumerate(input.split('\n\n')):
            p1,p2 = group.split('\n')
            p1 = eval(p1)
            p2 = eval(p2)
            print(f"[START]  LEFT = {p1} and RIGHT = {p2}")
            print(f'INDEX = {i}')
            if compare(p1,p2) == -1:
                result += 1 + i
        print(f'RESULT is {result}')


def compare(p1: int|List, p2):
    # both are ints
    print(f"[compare2]  LEFT = {p1} and RIGHT = {p2}")
    if isinstance(p1, int) and isinstance(p2, int):
        if p1 > p2:
            return 1 
        elif p2 > p1:
            return -1
        else:
            return 0
    # both are lists
    elif isinstance(p1, list) and isinstance(p2, list):
        i = 0
        while i<len(p1) and i<len(p2):
            print(f'Im in a loop, comparing {p1[i]} and {p2[i]}')
            c = compare(p1[i],p2[i])
            i += 1
            if  c == -1:
                return -1
            elif c == 1:
                return 1
            # if items are equal, continue loop
        # if left out of items, return -1
        if i == len(p1) and i < len(p2):
            return -1
        # if right out of items, return 1
        elif i == len(p2) and i < len(p1):
            return 1
        # if both are  equal, return 0
        else:
            return 0
    elif isinstance(p1, int) and isinstance(p2, list):
        return compare([p1],p2)
    else:
        return compare(p1,[p2])



if __name__ == "__main__":
    main("input")
