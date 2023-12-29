from main import Valve, BFS


def test_BFS():
    bb = Valve('BB', 10, [])
    cc = Valve('CC', 10, [])
    adjacent = [bb,cc]
    root = Valve('AA', 0, adjacent)
    expected = 2
    actual = BFS(root, 'BB')
    assert expected == len(actual)
