from main import create_tree


def test_tree():
    root = create_tree('test_input')
    root.print_itself()
    assert root.dirs[0].name == 'bntdgzs'
    assert len(root.dirs) == 1
