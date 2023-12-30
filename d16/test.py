from main import Valve, BFS


def split_string_every_second_char(input):
    n = 2
    return [input[i : i + n] for i in range(0, len(input), n)]


# def test_BFS():
#     bb = Valve('BB', 10, [])
#     cc = Valve('CC', 10, [])
#     adjacent = [bb,cc]
#     root = Valve('AA', 0, adjacent)
#     expected = 2
#     actual = BFS(root, 'BB')
#     assert expected == len(actual)


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
