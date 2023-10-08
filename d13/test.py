from main import explore
from main import parse_packet


#False def test_parse_one_list():
#     assert parse_packet("[]") == []
#     assert parse_packet("[5]") == [5]
#     assert parse_packet("[5,[3],2]") == [5, [3], 2]


def test_compare():

    # assert explore([[1,2,1],1], [[1,1,1,],1]) == False
    # assert explore([1, 1, 3, 1, 1] , [1, 1, 5, 1, 1]) == True
    # assert explore([1, 1, 5, 1, 1] , [1, 1, 3, 1, 1]) == False
    # assert explore([[[]]],[[]]) == False
    # assert explore([1], [1]) == True
    # assert explore([1], []) == False
    # assert explore([1, [2], [[3]]], []) == False
    # assert explore([1, [2], [[3]]], [2]) == True
    # assert explore([2,[]],[1,[[]]]) == False
    # assert explore([1],[2]) == True
    # assert explore([2],[1]) == False
    # assert explore([[[1]]],[[1]]) == True
    # assert explore([[1],[2,3,4]], [[1],1]) == False
    # assert explore([[1],[2,3,4]], [[1],4]) == True
    # assert explore([[1,2],[2,3,4]], [[1,1],4]) == False
    # assert explore([1, [2], [[3]]], [2]) == True
    # assert explore([],[]) == True
    # assert explore([[[]]],[[]]) == False
    # assert explore([[]],[[[]]]) == True
    # assert explore([2,[]],[1,[[]]]) == False
    # assert explore([1],[1]) == True
    # assert explore([1],[2]) == True
    # assert explore([2],[1]) == False
    # assert explore([[[1]]],[[1]]) == True # todo, this test is failing & perhaps solution to our failing algo
    # assert explore([[1],[2,3,4]], [[1],4]) == True
    # assert explore([[1],[2,3,4]], [[1],1]) == False
    # assert explore( [[],[2,7]] , [[2],[6]]) == True

    from main import compare2
    assert compare2([[1,2,1],1], [[1,1,1,],1]) == False
    assert compare2([1, 1, 3, 1, 1] , [1, 1, 5, 1, 1]) == True
    assert compare2([1, 1, 5, 1, 1] , [1, 1, 3, 1, 1]) == False
    assert compare2([[[]]],[[]]) == False
    assert compare2([1], [1]) == None
    assert compare2([1], []) == False
    assert compare2([1, [2], [[3]]], []) == False
    assert compare2([1, [2], [[3]]], [2]) == True
    assert compare2([2,[]],[1,[[]]]) == False
    assert compare2([1],[2]) == True
    assert compare2([2],[1]) == False
    assert compare2([[[1]]],[[1]]) == None
    assert compare2([[1],[2,3,4]], [[1],1]) == False
    assert compare2([[1],[2,3,4]], [[1],4]) == True
    assert compare2([[1,2],[2,3,4]], [[1,1],4]) == False
    assert compare2([1, [2], [[3]]], [2]) == True
    assert compare2([],[]) == None
    assert compare2([[[]]],[[]]) == False
    assert compare2([[]],[[[]]]) == True
    assert compare2([2,[]],[1,[[]]]) == False
    assert compare2([1],[1]) == None
    assert compare2([1],[2]) == True
    assert compare2([2],[1]) == False
    assert compare2([[[1]]],[[1]]) == None
    assert compare2([[1],[2,3,4]], [[1],4]) == True
    assert compare2([[1],[2,3,4]], [[1],1]) == False
    assert compare2( [[],[2,7]] , [[2],[6]]) == True
