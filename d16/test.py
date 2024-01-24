from main import Valve_Expected_Returns
from main import calculate_returns_for_a_single_turn, breadth_first_search, Valve, traceback, bfs_print_all_paths
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

@pytest.fixture
def valve_map_circular():
    aa = Valve('AA', 0, [])
    bb = Valve('BB', 10, [])
    cc = Valve('CC', 40, [])
    dd = Valve('DD', 100, [])
    ee = Valve('EE', 50, [])
    aa_adjacent = [bb,cc]
    bb_adjacent = [aa,ee]
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
    cache = {}
    results, cache = calculate_returns_for_a_single_turn(er, valve_map, cache)
    last = results[-1]
    assert 'EE' == last.name
    assert 300 == last.potential_flow
    assert 6 == last.remaining_turns


def test_breadth_first_search(valve_map):
    root = valve_map["AA"]
    path = breadth_first_search(valve_map, root, "EE")
    assert ('AACCDDEE', 3) == path

def test_traceback():
    parents = {}
    parents["BB"] = "AA"
    parents["CC"] = "BB"
    r = traceback(parents, "AA", "CC")
    assert ["AA", "BB", "CC"] == r

def test_bfs_print_all_paths(three_valves, valve_map, valve_map_circular):
    print(bfs_print_all_paths(three_valves, "AA", "CC"))
    print("============================================================")
    print( bfs_print_all_paths(valve_map, "AA", "DD"))
    print( bfs_print_all_paths(valve_map_circular, "AA", "DD"))

