from main import Valve, BFS
from main import calculate_returns


def test_BFS():
    map = {'AA': False,'BB': False,'CC': False,'DD': False,'EE': False,}
    bb = Valve('BB', 10, [])
    cc = Valve('CC', 10, [])
    adjacent = [bb,cc]
    root = Valve('AA', 0, adjacent)
    # one jump
    actual_path, jumps = BFS(root, 'BB', map.copy())
    assert 'AABB' == actual_path
    assert 1 == jumps
    print(f"END of TEST =======================")
    dd = Valve('DD', 10, [])
    cc.adjacent.append(dd)
    ee = Valve('EE', 10, [])
    dd.adjacent.append(ee)
    # two jumps
    actual_path, jumps = BFS(root, 'EE', map.copy())
    assert 'AACCDDEE' == actual_path
    assert 3 == jumps
    # and again, two jumps using same nodes
    # actual_path, jumps = BFS(root, 'EE')
    # assert 'AACCDDEE' == actual_path
    # assert 3 == jumps

# def test_calculate_returns_two_jumps():
#     aa = Valve('AA', 10, [])
#     bb = Valve('BB', 10, [])
#     cc = Valve('CC', 10, [])
#     dd = Valve('DD', 100, [])
#     aa_adjacent = [bb,cc]
#     bb_adjacent = [aa]
#     cc_adjacent = [aa,dd]
#     dd_adjacent = [cc]
#     aa.adjacent = aa_adjacent
#     bb.adjacent = bb_adjacent
#     cc.adjacent = cc_adjacent
#     dd.adjacent = dd_adjacent
#     map = {"AA": aa, "BB": bb, "CC": cc, "DD": dd}
#     # calc returns
#     results_map = calculate_returns(aa, map, 10)
#     for k,v in results_map.items():
#         print(k, " = ", v)
