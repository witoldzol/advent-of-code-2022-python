import re
from typing import List, Tuple


class Monkey():
    n: int
    items: List[int]
    operation: List[str]
    test: int

    def __init__(self) -> None:
        self.items = []


def main(file):
    monkeys: List[Monkey] = parse_monkeys_from_input(file)

def parse_monkeys_from_input(file) -> List[Monkey]:
    monkeys = []
    monkey = None
    with open(file, 'r') as f:
        for line in f:
            line = line.rstrip()
            if 'Monkey' in line:
                monkey = Monkey()
                _, i = line.split()
                monkey.n = int(list(i)[0])
            elif 'Starting' in line:
                matches = re.findall(r'\d+', line)
                if matches:
                    for item in matches:
                        monkey.items.append(item)
            elif 'Operation' in line:
                match = re.match(r'.*(old.+)', line)
                if match:
                    monkey.operation = match.groups()[0].split()
                    print(f'matched operation for monkey {monkey.n} => {monkey.operation}')
            monkeys.append(monkey)
    return []


if __name__ == "__main__":
    main('sample_input')
