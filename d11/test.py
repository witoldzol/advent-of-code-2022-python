from main import main


def test_main():
    assert main('sample_input') == 10605
    assert main('input') == 54752

