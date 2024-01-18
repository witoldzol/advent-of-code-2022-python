from typing import OrderedDict, Dict
from main import Valve_Expected_Returns
from main import filter_finished_paths, calculate_returns_for_a_single_turn, breadth_first_search, Valve
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

def test_calculate_returns_for_a_single_turn(valve_map):
    er = Valve_Expected_Returns("AA",0,10,"AA",0)
    results = calculate_returns_for_a_single_turn(er, valve_map)
    last = results[-1]
    assert 'EE' == last.name
    assert 300 == last.potential_flow
    assert 6 == last.remaining_turns


def test_finished_path(three_valves):
    print(three_valves)
    er = Valve_Expected_Returns("AA",0,4,"AA",0)
    results = calculate_returns_for_a_single_turn(er, three_valves)
    for o in results:
        print(o)
    second_run = []
    for r in results:
        assert r.finished == False
        r = calculate_returns_for_a_single_turn(r, three_valves)
        second_run.extend(r)
    for r in second_run:
        assert r.finished == True


def test_all_paths(valve_map):
    finished_paths = []
    er = Valve_Expected_Returns("AA",0,10,"AA",0)
    paths = calculate_returns_for_a_single_turn(er, valve_map)
    wip = []
    for _ in range(3):
        for p in wip if wip else paths:
            pp = calculate_returns_for_a_single_turn(p, valve_map)
            done, not_done = filter_finished_paths(pp)
            wip.extend(not_done)
            finished_paths.extend(done)
    all_ordered = sorted(finished_paths, key=lambda p: p.total_flow, reverse=True)
    assert 1120 == all_ordered[0].total_flow

def test_breadth_first_search(valve_map):
    root = valve_map["BB"]
    paths = breadth_first_search(valve_map, root, 'JJ')
    print(paths)
