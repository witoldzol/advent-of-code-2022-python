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
    # assert explore([1, [2], [[3]]], [2]) == False
    # assert explore([2,[]],[1,[[]]]) == False
    assert explore([1],[2]) == True
    # assert explore([2],[1]) == False
    # assert explore([[[1]]],[[1]]) == True
    # assert explore([[1],[2,3,4]], [[1],1]) == False
    # assert explore([[1],[2,3,4]], [[1],4]) == True
    # assert explore([[1,2],[2,3,4]], [[1,1],4]) == False
    # assert explore([[4,7,4],[6,1],[9,[],[[8,2],6],[[3,5,1,4],6,[10,3],4]],[[9,[],[2,4,10,3,7],[1,3,0,7,9],7],1],[[[10],[0,5,10,2],[2,5,2,5],[5,1,2,0,3]],1,[[2,2,8]],4,[8]]], [[0,[[],[],[9,4,1,2],7]]]) == True
    # assert explore([1, [2], [[3]]], [2]) == False
    # assert explore([1,2],4) == True
    # assert explore([[1],[2,3,4]],10) == False
    # assert explore([[1],[2,3,4]],1) == True
    # assert explore([],1) == False
    # assert compare([],[]) == True
    # assert compare([[[]]],[[]]) == False
    # assert compare([[]],[[[]]]) == True
    # assert compare([2,[]],[1,[[]]]) == False
    # assert compare([1],[1]) == True
    # assert compare([1],[2]) == True
    # assert compare([2],[1]) == False
    # assert compare([[[1]]],[[1]]) == True # todo, this test is failing & perhaps solution to our failing algo
    # assert compare([[1],[2,3,4]], [[1],4]) == True
    # assert compare([[1],[2,3,4]], [[1],1]) == False
