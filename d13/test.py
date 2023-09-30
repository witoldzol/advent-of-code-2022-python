from main import compare
from main import parse_packet


def test_parse_one_list():
    assert parse_packet('[]') == []
    assert parse_packet('[5]') == [5]
    assert parse_packet('[5,[3],2]') == [5, [3], 2]


def test_compare():
    assert compare([],[]) == True
    assert compare([[[]]],[[]]) == False
    assert compare([[]],[[[]]]) == True
    assert compare([2,[]],[1,[[]]]) == False
    assert compare([1],[1]) == True
    assert compare([1],[2]) == True
    assert compare([2],[1]) == False
    assert compare([[1],[2,3,4]], [[1],4]) == True
    assert compare([[1],[2,3,4]], [[1],1]) == False
    assert compare([[[1]]],[[1]]) == True # todo, this test is failing & perhaps solution to our failing algo

    #  [ [ [ 1 ]] ]
    #  [ [ [ 1 ]1 ] ]
    #
    # # how do we traverse nested arrays
    # [ [ 1 ] ]
    # [ 1 ]
    #
    # 1) comp [[1]] vs [1]
    # both are list
    # so we  iterate
    # compare
    # [1]
    # vs 
    # 1
    #
    # each com has a loop for list to list
    # each comp 
    #
    # can we write this iterativly?
    #
    #
    # parent => [c => [ cc ],c => [ccc]]
    # graph comparison algo
