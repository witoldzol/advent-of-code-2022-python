from collections import deque
from dataclasses import dataclass
from typing import List, Dict, Tuple
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
class Valve_Expected_Returns():
    name: str
    potential_flow: int
    remaining_turns: int
    path: str
    total_flow: int
    finished: bool = False
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


def traceback(child_to_parent: Dict[str, str], start: str, end: str) -> List[str]:
    current = end
    path = []
    for _ in range(len(child_to_parent) + 1):
        if current == start:
            path.append(current)
            return list(reversed(path))
        path.append(current)
        current = child_to_parent[current]
    return []


def breadth_first_search( graph: Dict[str, Valve], root: Valve, target: str) -> Tuple[str,int]:
    path = root.name
    visited = set()
    queue = deque()
    queue.append(path)
    while queue:
        path = queue.popleft()
        node_name = path[-2:]
        node = graph[node_name]
        visited.add(node)
        if node_name == target:
            return (path, (len(path) // 2) - 1)
        for c in node.adjacent:
            if c not in visited:
                new_path = path + c.name
                queue.append(new_path)
    return ("", -1)


def filter_finished_paths2(paths: List[Tuple[Valve_Expected_Returns,Valve_Expected_Returns]]) -> \
Tuple[
    List[Tuple[Valve_Expected_Returns,Valve_Expected_Returns]],
    List[Tuple[Valve_Expected_Returns,Valve_Expected_Returns]]
]:
    done = []
    not_done = []
    for p in paths:
        p1, p2 = p
        if p1.finished and p2.finished:
            done.append(p)
        else:
            not_done.append(p)
    return done, not_done


def filter_finished_paths(paths: List[Valve_Expected_Returns]) -> Tuple[List[Valve_Expected_Returns], List[Valve_Expected_Returns]]:
    done = []
    not_done = []
    for path in paths:
        if path.finished:
            done.append(path)
        else:
            not_done.append(path)
    return done, not_done


def calculate_returns_for_a_single_turn2(
        starts: Tuple[Valve_Expected_Returns, Valve_Expected_Returns],
        map: Dict[str, Valve],
        path_cache
    ) -> Tuple[List[Tuple[Valve_Expected_Returns,Valve_Expected_Returns]],Dict[str,str]]:
    results = []
    # if we have only 2 turns left, even if we have a place to go, it will not 'tick' to give us any flow -> skip it
    my_start, elephant_start = starts
    # if we are done
    my_paths = []
    if (my_start.remaining_turns <= 2 or my_start.finished): 
        my_finished_path = Valve_Expected_Returns(my_start.name, 0, 0, my_start.path, my_start.total_flow, True)
        # and elephant is done, return
        if (elephant_start.remaining_turns <= 2 or elephant_start.finished):
            elephant_finished_path = Valve_Expected_Returns(elephant_start.name, 0, 0, elephant_start.path, elephant_start.total_flow, True)
            return [(my_finished_path, elephant_finished_path)], path_cache
        # but elephant is not done
        else:
            my_paths.append(my_finished_path)
    # MY PATH
    start = my_start
    for valve in map.values():
        if my_paths: # if we finished out paths, end loop and move to elephant paths
            break
        if valve.name == start.name or valve.name in start.path or valve.name in elephant_start.path: # check if start position or already visited by me or elephant
            continue
        start_valve = map[start.name]
        start_valve_name = start_valve.name
        target_valve = valve.name
        entry = start_valve_name + target_valve
        if  entry in path_cache:
            path_to_valve = path_cache[entry]
        else:
            path_to_valve = breadth_first_search(map, start_valve, target_valve)
            path_cache[entry] = path_to_valve
        log.debug(f"path to valve {valve.name} takes {path_to_valve[1]} turns + 1 turn to turn on the valve")
        if not path_to_valve:
            raise Exception(f"Unable to find path to valve {valve.name}")
        _, turns_to_get_to_valve = path_to_valve
        turns_to_get_to_valve += 1  # one extra turn to activate the valve
        remaining_turns = start.remaining_turns - turns_to_get_to_valve
        log.debug(f"remaining turns for node {valve.name} is {remaining_turns}")
        potential_flow = valve.rate * remaining_turns
        # either invalid or pointless path - skip it
        if potential_flow <= 0:
            continue
        log.debug(f"potential flow for node {valve.name} is {potential_flow}")
        current_path = start.path + valve.name
        updated_flow = potential_flow + start.total_flow if potential_flow >= 0 else start.total_flow
        expected_returns = Valve_Expected_Returns(valve.name, potential_flow, remaining_turns, current_path, updated_flow, False)
        my_paths.append(expected_returns)
    ###### ELEPHANT PATH
    start = elephant_start
    # for every path we took, we now calc potential elephant paths
    for my_path in my_paths:
        for valve in map.values():
            if valve.name == start.name or valve.name in start.path or valve.name in my_path.path: # check if start position or already visited by me or elephant
                continue
            start_valve = map[start.name]
            start_valve_name = start_valve.name
            target_valve = valve.name
            entry = start_valve_name + target_valve
            if  entry in path_cache:
                path_to_valve = path_cache[entry]
            else:
                path_to_valve = breadth_first_search(map, start_valve, target_valve)
                path_cache[entry] = path_to_valve
            log.debug(f"path to valve {valve.name} takes {path_to_valve[1]} turns + 1 turn to turn on the valve")
            if not path_to_valve:
                raise Exception(f"Unable to find path to valve {valve.name}")
            _, turns_to_get_to_valve = path_to_valve
            turns_to_get_to_valve += 1  # one extra turn to activate the valve
            remaining_turns = start.remaining_turns - turns_to_get_to_valve
            log.debug(f"remaining turns for node {valve.name} is {remaining_turns}")
            potential_flow = valve.rate * remaining_turns
            # either invalid or pointless path - skip it
            if potential_flow <= 0:
                continue
            log.debug(f"potential flow for node {valve.name} is {potential_flow}")
            current_path = start.path + valve.name
            updated_flow = potential_flow + start.total_flow if potential_flow >= 0 else start.total_flow
            elephant_path = Valve_Expected_Returns(valve.name, potential_flow, remaining_turns, current_path, updated_flow, False)
            my_path_and_elephant_path = (my_path, elephant_path)
            results.append(my_path_and_elephant_path)
    if not results:
        my_finished_path = Valve_Expected_Returns(start.name, 0, 0, start.path, start.total_flow, True)
        elephant_finished_path = Valve_Expected_Returns(elephant_start.name, 0, 0, elephant_start.path, elephant_start.total_flow, True)
        me_and_elephant = my_finished_path, elephant_finished_path
        return [me_and_elephant], path_cache
    return results, path_cache

def calculate_returns_for_a_single_turn(
    start: Valve_Expected_Returns,
    map: Dict[str, Valve],
    path_cache
    ) -> Tuple[List[Valve_Expected_Returns], Dict[str,str]]:
    results = []
    # if we have only 2 turns left, even if we have a place to go, it will not 'tick' to give us any flow -> skip it
    if start.remaining_turns <= 2 or start.finished:
        finished_path = Valve_Expected_Returns(start.name, 0, 0, start.path, start.total_flow, True)
        return [finished_path], path_cache
    for valve in map.values():
        if valve.name == start.name or valve.name in start.path: # check if start position or already visited
            continue
        start_valve = map[start.name]
        start_valve_name = start_valve.name
        target_valve = valve.name
        entry = start_valve_name + target_valve
        if  entry in path_cache:
            path_to_valve = path_cache[entry]
        else:
            path_to_valve = breadth_first_search(map, start_valve, target_valve)
            path_cache[entry] = path_to_valve
        log.debug(f"path to valve {valve.name} takes {path_to_valve[1]} turns + 1 turn to turn on the valve")
        if not path_to_valve:
            raise Exception(f"Unable to find path to valve {valve.name}")
        _, turns_to_get_to_valve = path_to_valve
        turns_to_get_to_valve += 1  # one extra turn to activate the valve
        remaining_turns = start.remaining_turns - turns_to_get_to_valve
        log.debug(f"remaining turns for node {valve.name} is {remaining_turns}")
        potential_flow = valve.rate * remaining_turns
        # either invalid or pointless path - skip it
        if potential_flow <= 0:
            continue
        log.debug(f"potential flow for node {valve.name} is {potential_flow}")
        current_path = start.path + valve.name
        updated_flow = potential_flow + start.total_flow if potential_flow >= 0 else start.total_flow
        valve_exprected_returns = Valve_Expected_Returns(valve.name, potential_flow, remaining_turns, current_path, updated_flow, False)
        results.append(valve_exprected_returns)
    if not results:
        finished_path = Valve_Expected_Returns(start.name, 0, 0, start.path, start.total_flow, True)
        return [finished_path], path_cache
    return results, path_cache


def calculate_returns_for_all_paths(total_turns:int, valve_map: Dict[str,Valve]):
    cache = {}
    my_start = Valve_Expected_Returns("AA", 0, total_turns, "AA", 0)
    elephant_start = Valve_Expected_Returns("AA", 0, total_turns, "AA", 0)
    initial_paths, cached_paths = calculate_returns_for_a_single_turn2((my_start, elephant_start), valve_map, cache)
    cache = cache | cached_paths
    finished_paths = []
    wip = []
    for _ in range(len(valve_map)):
        wip_temp = []
        for p in wip if wip else initial_paths:
            pp, cached_paths = calculate_returns_for_a_single_turn2(p, valve_map, cache)
            cache = cache | cached_paths
            done, not_done = filter_finished_paths2(pp)
            not_done = sorted(not_done, key=lambda x: x.total_flow, reverse=True)
            not_done = not_done[:3]
            wip_temp.extend(not_done)
            finished_paths.extend(done)
        initial_paths = []
        wip = wip_temp
    all_ordered = sorted(finished_paths, key=lambda p: p.total_flow, reverse=True)
    return all_ordered[:3]

def main(input):
    _, valves = build_valve_graph(input)
    r = calculate_returns_for_all_paths(26,valves)
    for o in r:
        print(o)


if __name__ == "__main__":
    input = "sample_input"
    input = "input"
    main(input)
