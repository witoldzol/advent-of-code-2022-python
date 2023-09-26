from typing import List
import re


def main(filename):
    indices = []
    with open(filename, "r") as f:
        packet = []
        for line in f:
            line = line.rstrip()
            if is_empty_line(line):
                print("emtpy linie ", line)
                continue
            packet.append(line)
            if len(packet) == 2:
                indices.append(compare(packet))
                packet = []
    print(f"found {len(indices)} packet pairs in order")


def is_empty_line(line: str):
    return re.match(r"^$", line)


def compare(packets: List[str]) -> int:
    print("comparing packets ", packets)
    return 0


if __name__ == "__main__":
    main("sample_input")
