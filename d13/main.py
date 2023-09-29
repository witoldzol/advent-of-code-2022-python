from typing import List, TypeVar
import re
from re import Match
from dataclasses import dataclass


@dataclass
class Token:
    parent: "Token"
    val: List


def main(filename):
    indices = []
    with open(filename, "r") as f:
        packets = []
        for line in f:
            line = line.rstrip()
            if is_empty_line(line):
                continue
            packets.append(line)
            if len(packets) == 2:
                result = compare(packets)
                indices.append(result)
                packets = []
    print(f"found {len(indices)} packets pairs in order")


def compare(packets: List[str]) -> int:
    x, y = packets
    x_tokens = parse_packet(x)
    y_tokens = parse_packet(y)
    # print(x_tokens, ' , ', y_tokens)

    return 0


def is_empty_line(line: str) -> Match[str] | None:
    return re.match(r"^$", line)


def parse_packet(packet: str) -> List:
    if not packet:
        return
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
    main("sample_input")
