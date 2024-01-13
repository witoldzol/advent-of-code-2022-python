from typing import OrderedDict, Dict
from main import Valve, BFS
from main import calculate_returns, calculate_returns_for_a_single_turn, filter_finished_paths, calculate_returns_for_a_single_turn2
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

def test_filter_finished_paths(valve_map):
    finished_paths = []
    paths = calculate_returns_for_a_single_turn(valve_map["AA"], valve_map, 10 )
    assert 4 == len(paths)
    done, not_done = filter_finished_paths(paths)
    finished_paths.extend(done)
    assert 0 == len(done)
    assert 4 == len(not_done)
    # 2
    all = []
    for p in not_done:
        valve = valve_map[p.name]
        paths = calculate_returns_for_a_single_turn(valve, valve_map, p.remaining_turns, p.path, p.total_flow)
        all.extend(paths)
    assert 12 == len(all)
    done, not_done = filter_finished_paths(all)
    finished_paths.extend(done)
    assert 1 == len(done)
    assert 11 == len(not_done)
    # 3
    all = []
    for p in not_done:
        valve = valve_map[p.name]
        paths = calculate_returns_for_a_single_turn(valve, valve_map, p.remaining_turns, p.path, p.total_flow)
        all.extend(paths)
    assert 21 == len(all)
    done, not_done = filter_finished_paths(all)
    assert 10 == len(done)
    finished_paths.extend(done)
    assert 11 == len(not_done)
    for p in not_done:
        print(p)
    # 4
    # all = []
    # for p in not_done:
    #     valve = valve_map[p.name]
    #     paths = calculate_returns_for_a_single_turn(valve, valve_map, p.remaining_turns, p.path, p.total_flow)
    #     all.extend(paths)
    # assert 21 == len(all)
    # done, not_done = filter_finished_paths(all)
    # assert 10 == len(done)
    # finished_paths.extend(done)
    # assert 11 == len(not_done)


def test_all_paths(valve_map):
    finished_paths = []
    paths = calculate_returns_for_a_single_turn(valve_map["AA"], valve_map, 10 )
    wip = []
    for _ in range(3):
        for p in wip if wip else paths:
            pp = calculate_returns_for_a_single_turn2(p, valve_map)
            done, not_done = filter_finished_paths(pp)
            wip.extend(not_done)
            finished_paths.extend(done)
    all_ordered = sorted(finished_paths, key=lambda p: p.total_flow, reverse=True)
    assert 1120 == all_ordered[0].total_flow
