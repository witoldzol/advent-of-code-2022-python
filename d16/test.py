from main import Valve, BFS
from main import split_string_every_second_char


def test_BFS():
    bb = Valve('BB', 10, [])
    cc = Valve('CC', 10, [])
    adjacent = [bb,cc]
    root = Valve('AA', 0, adjacent)
    actual = BFS(root, 'BB')
    assert 'AABB' == actual


def test_split():
    actual = split_string_every_second_char("AABB")
    expected = 2
    assert expected == len(actual)
    actual = split_string_every_second_char("")
    expected = 0
    assert expected == len(actual)
    actual = split_string_every_second_char("AABBCCDD")
    expected = 4
    assert expected == len(actual)
