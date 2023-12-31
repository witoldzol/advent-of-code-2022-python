from main import Valve, BFS
from main import calculate_returns


def test_BFS():
    bb = Valve('BB', 10, [])
    cc = Valve('CC', 10, [])
    adjacent = [bb,cc]
    root = Valve('AA', 0, adjacent)
    # one jump
    actual_path, jumps = BFS(root, 'BB')
    assert 'AABB' == actual_path
    assert 1 == jumps
    dd = Valve('DD', 10, [])
    cc.adjacent.append(dd)
    ee = Valve('EE', 10, [])
    dd.adjacent.append(ee)
    # two jumps
    actual_path, jumps = BFS(root, 'EE')
    assert 'AACCDDEE' == actual_path
    assert 3 == jumps

def test_calculate_returns_two_jumps():
    aa = Valve('AA', 10, [])
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
    for k,v in results_map.items():
        print(k, " = ", v)
