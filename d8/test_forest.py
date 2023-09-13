from main import count_visible_trees


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
