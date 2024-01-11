from typing import OrderedDict, Dict
from main import Valve, BFS
from main import calculate_returns, calculate_returns_for_a_single_turn
import pytest

@pytest.fixture
def valve_map():
    aa = Valve('AA', 0, [])
    bb = Valve('BB', 10, [])
    cc = Valve('CC', 40, [])
    dd = Valve('DD', 100, [])
    ee = Valve('EE', 50, [])
    aa_adjacent = [bb,cc]
    bb_adjacent = [aa]
    cc_adjacent = [aa,dd]
    dd_adjacent = [cc,ee]
    ee_adjacent = [dd]
    aa.adjacent = aa_adjacent
    bb.adjacent = bb_adjacent
    cc.adjacent = cc_adjacent
    dd.adjacent = dd_adjacent
    ee.adjacent = ee_adjacent
    map = {"AA": aa, "BB": bb, "CC": cc, "DD": dd, "EE": ee}
    yield map

def test_BFS():
    map = {
        "AA": False,
        "BB": False,
        "CC": False,
        "DD": False,
        "EE": False,
    }
    bb = Valve("BB", 10, [])
    cc = Valve("CC", 10, [])
    adjacent = [bb, cc]
    root = Valve("AA", 0, adjacent)
    # one jump
    actual_path, jumps = BFS(root, "BB")
    assert "AABB" == actual_path
    assert 1 == jumps
    dd = Valve("DD", 10, [])
    cc.adjacent.append(dd)
    ee = Valve("EE", 10, [])
    dd.adjacent.append(ee)
    # two jumps
    actual_path, jumps = BFS(root, "EE")
    assert "AACCDDEE" == actual_path
    assert 3 == jumps
    # and again, two jumps using same nodes
    actual_path, jumps = BFS(root, "EE")
    assert "AACCDDEE" == actual_path
    assert 3 == jumps


def test_calculate_returns_two_jumps(valve_map):
    results_map = calculate_returns(valve_map["AA"], valve_map, 10)
    assert 700 == results_map["DD"]


def test_calculate_returns_three_jumps(valve_map):
    results_map = calculate_returns(valve_map["AA"], valve_map, 10)
    assert 700 == results_map["DD"]
    assert 250 == results_map["EE"]


def test_calculate_returns_for_a_single_turn(valve_map):
    results = calculate_returns_for_a_single_turn(valve_map["AA"], valve_map, 10)
    assert 4 == len(results)
    last = results[-1]
    assert 'EE' == last.name
    assert 300 == last.potential_flow
    assert 6 == last.remaining_turns


def test_different_paths(valve_map):
    # generate initial paths
    results = calculate_returns_for_a_single_turn(valve_map["AA"], valve_map, 10)
    assert 4 == len(results)
    last = results[-1]
    assert 'EE' == last.name
    assert 300 == last.potential_flow
    assert 6 == last.remaining_turns
    # calculate returns for different starts
    sums = {}
    for valve in results:
        od = OrderedDict()
        od[valve.name] = valve.potential_flow
        sum = valve.potential_flow
        path = ''
        returns: Tuple[Dict[str, int], int] = calculate_returns(valve_map[valve.name], valve_map, valve.remaining_turns, od)
        for k,v in returns.items():
            path += k
            sum += v
        sums[path] = sum
    assert sums == {'BBDDEE': 660, 'CCDDEE': 1440, 'DDEECC': 1730, 'EEDDCC': 1080}


def test_all_paths(valve_map):
    all_returns = []
    paths = calculate_returns_for_a_single_turn(valve_map["AA"], valve_map, 10 )
    for p in paths:
        last_visited = p.name[-2:]
        path = calculate_returns_for_a_single_turn(valve_map[last_visited], valve_map, p.remaining_turns, p.path, p.total_flow)
        for pp in path:
            all_returns.append(pp)
    for p in all_returns:
        last_visited = p.name[-2:]
        path = calculate_returns_for_a_single_turn(valve_map[last_visited], valve_map, p.remaining_turns, p.path, p.total_flow)
        for pp in path:
            all_returns.append(pp)
    for p in all_returns:
        last_visited = p.name[-2:]
        path = calculate_returns_for_a_single_turn(valve_map[last_visited], valve_map, p.remaining_turns, p.path, p.total_flow)
        for pp in path:
            all_returns.append(pp)
    all_ordered = sorted(all_returns, key=lambda p: p.total_flow, reverse=True)
    for o in all_ordered:
        print(o)
    assert 1120 == all_ordered[0].total_flow


