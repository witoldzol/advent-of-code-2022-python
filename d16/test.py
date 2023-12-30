from main import Valve, BFS
from main import split_string_every_second_char


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
