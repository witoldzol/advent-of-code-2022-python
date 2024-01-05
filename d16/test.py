from typing import OrderedDict
from main import Valve, BFS
from main import calculate_returns, calculate_returns2, calculate_returns3


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


def test_calculate_returns_two_jumps():
    aa = Valve('AA', 0, [])
    bb = Valve('BB', 10, [])
    cc = Valve('CC', 10, [])
    dd = Valve('DD', 100, [])
    aa_adjacent = [bb,cc]
    bb_adjacent = [aa]
    cc_adjacent = [aa,dd]
    dd_adjacent = [cc]
    aa.adjacent = aa_adjacent
    bb.adjacent = bb_adjacent
    cc.adjacent = cc_adjacent
    dd.adjacent = dd_adjacent
    map = {"AA": aa, "BB": bb, "CC": cc, "DD": dd}
    # calc returns
    results_map = calculate_returns(aa, map, 10)
    assert 700 == results_map["DD"]


def test_calculate_returns_three_jumps():
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
    # calc returns
    results_map = calculate_returns(aa, map, 10)
    assert 700 == results_map["DD"]
    assert 250 == results_map["EE"]


def test_calculate_returns2_two_jumps():
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
    # calc returns
    results_map, remaining_turns = calculate_returns2(aa, map, 10, OrderedDict())
    assert 700 == results_map["DD"]
    start_node_name = list(results_map.keys())[-1]
    start_node = map[start_node_name]
    results_map, remaining_turns = calculate_returns2(start_node, map, remaining_turns, results_map)
    assert 250 == results_map["EE"]


def test_calculate_returns3_two_jumps():
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
    # calc returns
    results = calculate_returns3(aa, map, 10)
    assert 4 == len(results)
    last = results[-1]
    assert 'EE' == last.name
    assert 300 == last.potential_flow
    assert 6 == last.remaining_turns
