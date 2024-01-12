from dataclasses import dataclass
from typing import List, Dict, Set, Tuple
from collections import OrderedDict
import pudb
import logging

log = logging.getLogger()
log.setLevel("DEBUG")


class Valve:
    def __init__(self, name: str, rate: int, adjacent: List["Valve"] = None) -> None:
        self.adjacent = adjacent
        self.name = name
        self.rate = rate
    def __repr__(self) -> str:
        return f"Valve(name={self.name}, rate={self.rate}, adjacent={[v.name for v in self.adjacent]})"


@dataclass(frozen=True)
class Valve_Exprected_Returns():
    name: str
    potential_flow: int
    remaining_turns: int
    path: str
    total_flow: int
    def __repr__(self):
        return f"Valve_Exprected_Returns(name={self.name}, potential_flow={self.potential_flow}, remaining_turns={self.remaining_turns}, path={self.path}, total_flow={self.total_flow}"


def build_valve_graph(filename: str) -> Tuple[Valve, Dict[str, Valve]]:
    valves = {}
    data = open(filename, "r").read().strip()
    lines = data.split("\n")
    adjacent_dict = {}
    for l in lines:
        chunks = l.split(" ")
        name = chunks[1]
        _, rate = chunks[4].split("=")
        rate = int(rate[:-1])
        adjacent = chunks[9:]
        adjacent = " ".join(adjacent)
        adjacent = adjacent.split(",")
        adjacent = [x.strip() for x in adjacent]
        valves[name] = Valve(name, rate)
        adjacent_dict[name] = adjacent
    for valve in valves.values():
        valve.adjacent = []
        adjacent_valves = adjacent_dict[valve.name]
        for name in adjacent_valves:
            valve.adjacent.append(valves[name])
    return valves["AA"], valves


def BFS(
    root: Valve,
    target: str,
    map: Dict[str, bool] | None = None,
    path: str = "",
    jumps: int = -1,
) -> Tuple[str, int] | None:
    if not map:
        map = {}
    if not root:
        return "", jumps
    path += root.name
    map[root.name] = True
    jumps += 1
    if root.name == target:
        return path, jumps
    result = ""
    for v in root.adjacent:
        if not v.name in map:
            result = BFS(v, target, map, path, jumps)
            if result:
                return result


def print_path_and_total(input: OrderedDict) -> None:
    total = 0
    path = 'AA'
    for k,v in input.items():
        total += v
        path += k
    print(f"PATH={path}, TOTAL={total}")


def calculate_returns(
    start: Valve, map: Dict[str, Valve], max_turns: int, max_returns_map: OrderedDict = None
    ) -> Tuple[Dict[str, int], int]:
    log.info(f"START NODE = {start}, MAX_TURNS = {max_turns}")
    if not max_returns_map:
        max_returns_map = OrderedDict()
    max_flow = 0
    max_value_valve = ""
    jump = 0
    turn = max_turns
    for _ in range(len(map)):
        log.debug(f"Turns left == {turn}, current valve is {start.name}")
        for valve in map.values():
            if valve.name == start.name or \
               valve.rate == 0 or \
               valve.name in max_returns_map:
                continue
            path_to_valve = BFS(start, valve.name)
            log.debug(f"path to valve {valve.name} takes {path_to_valve[1]} turns + 1 turn to turn on the valve")
            if not path_to_valve:
                raise Exception(f"Unable to find path to valve {valve.name}")
            _, turns_to_get_to_valve = path_to_valve
            turns_to_get_to_valve += 1  # one extra turn to activate the valve
            remaining_turns = turn - turns_to_get_to_valve
            log.debug(f"remaining turns for node {valve.name} is {remaining_turns}")
            potential_flow = valve.rate * remaining_turns
            log.debug(f"potential flow for node {valve.name} is {potential_flow}")
            if potential_flow > max_flow:
                max_flow = potential_flow
                max_value_valve = valve.name
                jump = turns_to_get_to_valve
        # exit early if more turns than valves
        turn -= jump
        if not max_value_valve:
            print("===================")
            print(f"{max_returns_map=}")
            print_path_and_total(max_returns_map)
            print("===================")
            return max_returns_map
        max_returns_map[max_value_valve] = max_flow
        start = map[max_value_valve]
        max_flow = 0
        max_value_valve = ""
    # print("===================")
    # print(f"{max_returns_map=}")
    # print("===================")
    return max_returns_map, turn



def calculate_returns_for_a_single_turn(
    start: Valve,
    map: Dict[str, Valve],
    max_turns: int,
    path: str = '',
    total_flow: int = 0
    ) -> List[Valve_Exprected_Returns]:
    results = []
    if max_turns <= 0:
        return results
    if path == '':
        path = start.name
    for valve in map.values():
        if valve.name == start.name or valve.name in path: # check if start position or already visited 
            continue
        path_to_valve = BFS(start, valve.name)
        log.debug(f"path to valve {valve.name} takes {path_to_valve[1]} turns + 1 turn to turn on the valve")
        if not path_to_valve:
            raise Exception(f"Unable to find path to valve {valve.name}")
        _, turns_to_get_to_valve = path_to_valve
        turns_to_get_to_valve += 1  # one extra turn to activate the valve
        remaining_turns = max_turns - turns_to_get_to_valve
        if remaining_turns < 0:
            continue
        log.debug(f"remaining turns for node {valve.name} is {remaining_turns}")
        potential_flow = valve.rate * remaining_turns
        log.debug(f"potential flow for node {valve.name} is {potential_flow}")
        current_path = path + valve.name
        updated_flow = potential_flow + total_flow if potential_flow >= 0 else total_flow
        valve_exprected_returns = Valve_Exprected_Returns(valve.name, potential_flow, remaining_turns, current_path, updated_flow)
        results.append(valve_exprected_returns)
    return results


def select_best_paths(n: int, paths: List[Valve_Exprected_Returns]) -> List[Valve_Exprected_Returns]:
    sorted_paths = sorted(paths, key=lambda x: x.potential_flow, reverse=True)
    return sorted_paths[:n]


def main(input):
    root, valves = build_valve_graph(input)


if __name__ == "__main__":
    input = "sample_input"
    # input = "input"
    # input = "small_input"
    main(input)
