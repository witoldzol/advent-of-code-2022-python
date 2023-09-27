from typing import List, TypeVar
import re
from re import Match
from dataclasses import dataclass

@dataclass
class Token:
    parent: 'Token'
    val: str = ''


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
    x_output = parse_tokens(x_tokens)
    for t in x_tokens:
        print(t)
    return 0


# [[1],2]
def parse_tokens(tokens: List[Token]) -> List:
    out = []
    for t in tokens:
        match t:
            case t.root  == None:
                continue
        
        




def is_empty_line(line: str) -> Match[str] | None:
    return re.match(r"^$", line)


def is_open_bracket(c: str) -> bool:
    return c == "["


# [ - we open a new list, this is the new parent, everything afterwards goes inside of it
# ] - we close current parent list, we shift parent to it's parent
def parse_packet(packet: str): 
    tokens = []
    if not packet:
        return
    parent: Token = None
    for c in packet:
        match c:
            case '[':
                t = Token(parent, c)
                tokens.append(t)
                parent = t
            case ']':
                t = Token(parent, c)
                tokens.append(t)
                parent = parent.parent
            case '0':
                t = Token(parent, c)
                tokens.append
            case '1':
                t = Token(parent, c)
                tokens.append
            case '2':
                t = Token(parent, c)
                tokens.append
            case '3':
                t = Token(parent, c)
                tokens.append
            case '4':
                t = Token(parent, c)
                tokens.append
            case '5':
                t = Token(parent, c)
                tokens.append
            case '6':
                t = Token(parent, c)
                tokens.append
            case '7':
                t = Token(parent, c)
                tokens.append
            case '8':
                t = Token(parent, c)
                tokens.append
            case '9':
                t = Token(parent, c)
                tokens.append
            case ',':
                pass
            case _:
                raise Exception(f'Unknown input = {c}, please investigate!')
    return tokens


if __name__ == "__main__":
    main("sample_input")
