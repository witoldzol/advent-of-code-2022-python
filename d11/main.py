import re
import math
from typing import List


class Monkey():
    n: int
    items: List[int]
    operation: List[str]
    test: int
    test_true: int
    test_false: int
    inspect_counter: int = 0

    def __init__(self) -> None:
        self.items = []


    def recalculate_item_worry(self, item:int) -> int:
        first: int = item
        second: int  =  item if self.operation[2] == 'old' else int(self.operation[2])
        match self.operation[1]:
            case '+':
                return first + second
            case '*':
                return first * second
            case _:
                raise Exception(f'Found unknown operation {self.operation[1]}')


def main(file) -> int:
    monkeys: List[Monkey] = parse_monkeys_from_input(file)
    for _ in range(20):
        for m in monkeys:
            for i in m.items:
                m.inspect_counter += 1
                new_i = math.floor(m.recalculate_item_worry(i) / 3)
                if new_i % m.test == 0:
                    monkeys[m.test_true].items.append(new_i)
                else:
                    monkeys[m.test_false].items.append(new_i)
            m.items.clear()
    for m in monkeys:
        print(m.inspect_counter)
    counters = [m.inspect_counter for m in monkeys ]
    highest_two = sorted(counters)[-2:]
    result = highest_two[0] * highest_two[1]
    print('Solution is : ', result)
    return  result


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
                        monkey.items.append(int(item))
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
    main('input')
