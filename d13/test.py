from main import compare
from main import parse_packet


def test_parse_one_list():
    assert parse_packet('[]') == []
    assert parse_packet('[5]') == [5]
    assert parse_packet('[5,[3],2]') == [5, [3], 2]


def test_compare():
    assert compare([],[]) == True
    assert compare([1],[1]) == True
    assert compare([1],[2]) == True
