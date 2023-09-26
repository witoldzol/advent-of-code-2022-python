from typing import List
import re
from re import Match


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
                indices.append(compare(packets))
                packets = []
    print(f"found {len(indices)} packets pairs in order")


def is_empty_line(line: str) -> Match[str] | None:
    return re.match(r"^$", line)

def parse_packet(packet: str):
    if not packet:
        return
    result = None
    for c in packet:
        if c == '[' :
            if not result:
                result = []
    return result


def compare(packets: List[str]) -> int:
    x,y = packets
    return parse_packet(x)
    # print("packet 1", x)
    # print("packet 2", y)
    # return 0


if __name__ == "__main__":
    main("sample_input")
