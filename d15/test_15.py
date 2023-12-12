from main import MAX_REGION
from main import merge_ranges
from main import generate_manhatan_lengths_slow
from main import fill_the_borders2
from main import generate_manhatan_lengths


def test_generate_manhatan_lengths():
    coords = (2, 2, 2, 2)
    actual = generate_manhatan_lengths(coords, 3)
    assert [] == actual
    coords = (2, 2, 2, 3)
    actual = generate_manhatan_lengths(coords, 3)
    expected = [(2, 3)]
    assert sorted(expected) == sorted(actual)
    coords = (2, 2, 2, 4)
    actual = generate_manhatan_lengths(coords, 3)
    expected = [(1, 3), (3, 3)]
    assert sorted(expected) == sorted(actual)
    coords = (2, 2, 2, 4)
    actual = generate_manhatan_lengths(coords, 30)
    expected = []
    assert sorted(expected) == sorted(actual)


def test_merge_ranges():
    # one existing range, contains new range
    new_range = (2,4)
    existing_range = [(2,5)]
    actual = merge_ranges(new_range, existing_range)
    assert  [(2,5)] == actual

    # left extended
    new_range = (1,4)
    existing_range = [(2,5)]
    actual = merge_ranges(new_range, existing_range)
    assert  [(1,5)] == actual
    
    # right extended
    new_range = (3,6)
    existing_range = [(2,5)]
    actual = merge_ranges(new_range, existing_range)
    assert  [(2,6)] == actual

    # right extended multiple times
    new_range = (1,6)
    existing_range = [(1,2),(4,5)]
    actual = merge_ranges(new_range, existing_range)
    assert  [(1,6)] == actual

    # second item extended
    new_range = (4,6)
    existing_range = [(1,2),(4,5)]
    actual = merge_ranges(new_range, existing_range)
    assert  [(1,2),(4,6)] == actual

    # no-op, first item
    new_range = (1,2)
    existing_range = [(1,2),(4,5)]
    actual = merge_ranges(new_range, existing_range)
    assert  [(1,2),(4,5)] == actual

    # no-op, second item
    new_range = (4,5)
    existing_range = [(1,2),(4,5)]
    actual = merge_ranges(new_range, existing_range)
    assert  [(1,2),(4,5)] == actual

# def test_invert_map_row():
#     ranges = [(100,200)]
#     actual = invert_map_row(ranges)
#     assert [(0,99),(201,MAX_REGION)] == actual
#     ranges = [(100,200), (300,400)]
#     actual = invert_map_row(ranges)
#     assert [(0,99),(201,299),(401,MAX_REGION)] == actual
#     ranges = [(-100,50),(100,200), (300,400)]
#     actual = invert_map_row(ranges)
#     assert [(51,99),(201,299),(401,MAX_REGION)] == actual
#     ranges = [(-200,-100),(100,200), (300,400)]
#     actual = invert_map_row(ranges)
#     assert [(0,99),(201,299),(401,MAX_REGION)] == actual
