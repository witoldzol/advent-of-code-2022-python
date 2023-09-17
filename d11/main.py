import re
from pprint import pprint
from typing import List


class Monkey():
    n: int
    items: List[int]
    test: int
    operation: List[str]
    test: int
    test_true: int
    test_false: int

    def __init__(self) -> None:
        self.items = []


    def apply_operation(self, item:int) -> int:
        for o in self.operation:
            print(o)
        return 0


    def update_worry(self, item: int):
        return self.apply_operation(item)



def main(file):
    monkeys: List[Monkey] = parse_monkeys_from_input(file)
    for m in monkeys:
        for i in m.items:
            i = m.update_worry(i) # todo - continue from heere


def parse_monkeys_from_input(file) -> List[Monkey]:
    monkeys = []
    monkey = None
    with open(file, 'r') as f:
        for line in f:
            line = line.rstrip()
            if 'Monkey' in line:
                if monkey:
                    monkeys.append(monkey)
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
                    operation: List[str] = match.groups()[0].split()
                    monkey.operation = operation
            elif 'Test' in line:
                match = re.search(r'\D*(\d+)\D*', line)
                if match:
                    if len(match.groups()) > 1:
                        print(match.groups())
                        raise Exception('found too many test dividers')
                    test: int = int(match.groups()[0])
                    monkey.test = test 
                else:
                    raise Exception('Test value not found!')
            elif 'If true' in line:
                match = re.search(r'\D*(\d+)\D*', line)
                if match:
                    if len(match.groups()) > 1:
                        print(match.groups())
                        raise Exception('found too many monkey targets')
                    test_true: int = int(match.groups()[0])
                    monkey.test_true = test_true
            elif 'If false' in line:
                match = re.search(r'\D*(\d+)\D*', line)
                if match:
                    if len(match.groups()) > 1:
                        print(match.groups())
                        raise Exception('found too many monkey targets')
                    test_false: int = int(match.groups()[0])
                    monkey.test_false = test_false
            else:
                if line.strip(): # if line is not empty
                    print(line)
                    raise Exception('Unrecognized input detected')
    monkeys.append(monkey)
    return monkeys


if __name__ == "__main__":
    main('sample_input')
