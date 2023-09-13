from main import count_visible_trees

from main import main


def test_one_tree():
    forest = [[1]]
    assert count_visible_trees(forest) == 1

def test_two_trees():
    forest = [[1],[2]]
    assert count_visible_trees(forest) == 2

def test_two_by_two_trees():
    forest = [[1,1],[2,2]]
    assert count_visible_trees(forest) == 4

def test_three_by_three_trees_one_hidden():
    forest = [[1,1,1],
              [1,0,1],
              [2,2,2]]
    assert count_visible_trees(forest) == 8

def test_four_by_four_trees_two_hidden():
    forest = [[1,1,1,1],
              [1,0,0,1],
              [1,2,2,1],
              [2,2,2,2]]
    assert count_visible_trees(forest) == 14 

def test_four_by_four_trees_one_hidden():
    forest = [[1,1,1,1],
              [1,0,2,1],
              [1,2,2,1],
              [2,1,1,2]]
    assert count_visible_trees(forest) == 15 

def test_four_by_four_trees_one_hidden_bottom():
    forest = [[1,1,2,1],
              [1,0,2,1],
              [1,2,2,1],
              [2,1,1,2]]
    assert count_visible_trees(forest) == 15 

def test_four_by_four_trees_zero_hidden():
    forest = [[1,0,0,1],
              [1,1,1,1],
              [1,1,1,1],
              [2,0,0,2]]
    assert count_visible_trees(forest) == 16 

def test_five_by_five_trees_zero_hidden():
    forest = [[1,1,1,1,1],
              [1,2,3,2,1],
              [1,2,3,2,1],
              [1,2,3,2,1],
              [2,0,1,1,1]]
    assert count_visible_trees(forest) == 25

def test_five_by_five_trees_one_hidden():
    forest = [[1,1,1,1,1],
              [1,2,3,2,1],
              [1,2,0,2,1],
              [1,2,3,2,1],
              [2,0,1,1,1]]
    assert count_visible_trees(forest) == 24

def test_sample_input():
    # 30373
    # 25512
    # 65332
    # 33549
    # 35390
    assert main('sample_input') == 21

def test_five_by_five_trees_one_hidden_from_deep_below():
    forest = [[1,1,1,1,1],
              [1,2,3,2,1],
              [1,3,3,3,1],
              [1,2,2,1,0],
              [2,0,3,1,1]]
    assert count_visible_trees(forest) == 24

def test_five_by_five_trees_one_hidden_from_deep_left():
    forest = [[1,1,1,1,1],
              [1,2,3,2,1],
              [3,2,3,3,1],
              [1,1,3,1,0],
              [2,0,1,1,1]]
    assert count_visible_trees(forest) == 24
