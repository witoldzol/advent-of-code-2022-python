from main import count_visible_trees


def test_one_tree():
    forest = [[1]]
    assert count_visible_trees(forest) == 1

