from typing import Tuple, List
from main import invert_map_row
from main import MAX_REGION
from main import merge_ranges
from main import map_ranges
from main import merge_overlapping, is_overlapping
from main import generate_manhatan_lengths_slow
from main import fill_the_borders2
from main import generate_manhatan_lengths
from main import generate_manhatan_ranges


def test_generate_manhatan_lengths_slow():
    coords = (2, 2, 2, 2)
    actual = generate_manhatan_lengths_slow(coords)
    assert [] == actual
    coords = (2, 2, 3, 3)
    actual = generate_manhatan_lengths_slow(coords)
    expected = [(2, 4), (3, 1), (1, 1), (2, 0), (4, 2), (0, 2), (3, 3), (1, 3)]
    assert sorted(expected) == sorted(actual)
    coords = (2, 2, -1, -1)
    actual = generate_manhatan_lengths_slow(coords)
    expected = [
        (-4, 2),
        (-3, 1),
        (-3, 3),
        (-2, 0),
        (-2, 4),
        (-1, -1),
        (-1, 5),
        (0, -2),
        (0, 6),
        (1, -3),
        (1, 7),
        (2, -4),
        (2, 8),
        (3, -3),
        (3, 7),
        (4, -2),
        (4, 6),
        (5, -1),
        (5, 5),
        (6, 0),
        (6, 4),
        (7, 1),
        (7, 3),
        (8, 2),
    ]
    assert sorted(expected) == sorted(actual)


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


def test_fill_the_borders2():
    coords = {}
    m_lenghts = [(1736480, 2000000), (-1042974, 2000000)]
    fill_the_borders2(coords=coords, lens=m_lenghts)
    expected = 1736480 - (-1042974)
    assert expected == len(coords)
    subset_m_lenghts = [(1736480, 2000000), (-104297, 2000000)]
    fill_the_borders2(coords=coords, lens=subset_m_lenghts)
    assert expected == len(coords)


def test_manhatan_ranges():
    coords = (2, 2, 4, 4)
    actual = generate_manhatan_ranges(coords)
    assert (0, 4, 0, 4) == actual


def test_is_overlapping():
    from_map = (3, 6)
    new_range = (4, 6)
    actual = is_overlapping(new_range, from_map)
    assert actual == True

    from_map = (3, 6)
    new_range = (7, 9)
    actual = is_overlapping(new_range, from_map)
    assert actual == False


def test_merge_overlapping():
    from_map = (3, 6)
    new_range = (4, 7)
    assert (3, 7) == merge_overlapping(new_range, from_map)


def test_map_ranges():

    # ranges = [(2, 2, 4, 4)]
    # actual = map_ranges(ranges)
    # assert {2: [(4, 4)]} == actual

    ranges = [(2, 4, 4, 4), (2, 3, 4, 4)]
    actual = map_ranges(ranges)
    assert {2: [(4, 4)],
            3: [(4, 4)],
            4: [(4, 4)]} == actual

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

def test_invert_map_row():
    # map = (1, (100,200))
    actual = invert_map_row(1,(100,200))
    assert (1, (0,99),(201,MAX_REGION)) == actual
