from math import exp
from typing import Tuple
from main import generate_manhatan_lengths



def test_generate_manhatan_lengths():
    coords = (2,2,2,2)
    actual = generate_manhatan_lengths(coords)
    assert [] == actual

    coords = (2,2,2,3)
    actual = generate_manhatan_lengths(coords)
    expected = [(3, 2), (2, 3), (1, 2), (2, 1)]
    assert sorted(expected) == sorted(actual)

    coords = (2,2,2,4)
    actual = generate_manhatan_lengths(coords)
    expected = [(0, 2), (1, 1), (1, 3), (2, 0), (2, 4), (3, 1), (3, 3), (4, 2)]
    assert sorted(expected) == sorted(actual)
