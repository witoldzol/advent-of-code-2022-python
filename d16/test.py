from typing import OrderedDict, Dict
from main import Valve_Expected_Returns
from main import Valve, BFS
from main import calculate_returns, filter_finished_paths, calculate_returns_for_a_single_turn2
import pytest

@pytest.fixture
def three_valves():
    aa = Valve('AA', 0, [])
    bb = Valve('BB', 10, [])
    cc = Valve('CC', 40, [])
    aa_adjacent = [bb,cc]
    bb_adjacent = [aa]
    cc_adjacent = [aa]
    aa.adjacent = aa_adjacent
    bb.adjacent = bb_adjacent
    cc.adjacent = cc_adjacent
    map = {"AA": aa, "BB": bb, "CC": cc}
    yield map

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
    er = Valve_Expected_Returns("AA",0,10,"AA",0)
    results = calculate_returns_for_a_single_turn2(er, valve_map)
    last = results[-1]
    assert 'EE' == last.name
    assert 300 == last.potential_flow
    assert 6 == last.remaining_turns


def test_different_paths(valve_map):
    # generate initial paths
    er = Valve_Expected_Returns("AA",0,10,"AA",0)
    results = calculate_returns_for_a_single_turn2(er, valve_map)
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

def test_finished_path(three_valves):
    print(three_valves)
    er = Valve_Expected_Returns("AA",0,4,"AA",0)
    results = calculate_returns_for_a_single_turn2(er, three_valves)
    for o in results:
        print(o)
    second_run = []
    for r in results:
        assert r.finished == False
        r = calculate_returns_for_a_single_turn2(r, three_valves)
        second_run.extend(r)
    for r in second_run:
        assert r.finished == True


def test_all_paths(valve_map):
    finished_paths = []
    er = Valve_Expected_Returns("AA",0,10,"AA",0)
    paths = calculate_returns_for_a_single_turn2(er, valve_map)
    wip = []
    for _ in range(3):
        for p in wip if wip else paths:
            pp = calculate_returns_for_a_single_turn2(p, valve_map)
            done, not_done = filter_finished_paths(pp)
            wip.extend(not_done)
            finished_paths.extend(done)
    all_ordered = sorted(finished_paths, key=lambda p: p.total_flow, reverse=True)
    assert 1120 == all_ordered[0].total_flow
