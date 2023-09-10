from main import create_tree


def test_tree_one_folder():
    root = create_tree('test_input')
    root.print_itself()
    assert root.dirs[0].name == 'bntdgzs'
    assert len(root.dirs) == 1

def test_tree_three_folders():
    root = create_tree('test_input_2')
    root.print_itself()
    assert root.dirs[0].name == 'a'
    assert len(root.dirs) == 2 # / has a & b
    assert len(root.dirs[1].dirs) == 1 # b has c
