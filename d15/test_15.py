from typing import Tuple
from main import generate_manhatan_lengths



def test_generate_manhatan_lengths():
    coords = (2,2,2,2)
    actual = generate_manhatan_lengths(coords)
    assert [] == actual

    coords = (2,2,2,3)
    actual = generate_manhatan_lengths(coords)
    assert [(2, 3), (3, 2), (1, 2), (2, 1)] == actual
