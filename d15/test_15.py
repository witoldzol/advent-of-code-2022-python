from math import exp
from typing import Tuple
# from d15.main import fill_the_borders2
from main import fill_the_borders2
from main import generate_manhatan_lengths

from unittest import mock

@mock.patch('main.ROW', 3) # todo - make a param, handle case when row is outside of bounds
def test_generate_manhatan_lengths():
    coords = (2, 2, 2, 2)
    actual = generate_manhatan_lengths(coords)
    assert [] == actual
    coords = (2, 2, 2, 3)
    actual = generate_manhatan_lengths(coords)
    expected = [(3, 2), (2, 3), (1, 2), (2, 1)]
    assert sorted(expected) == sorted(actual)
    coords = (2, 2, 2, 4)
    actual = generate_manhatan_lengths(coords)
    expected = [(0, 2), (1, 1), (1, 3), (2, 0), (2, 4), (3, 1), (3, 3), (4, 2)]
    assert sorted(expected) == sorted(actual)

def test_fill_the_borders2():
    coords = {}
    m_lenghts = [(1736480, 2000000), (-1042974, 2000000)]
    fill_the_borders2(coords=coords, lens=m_lenghts)
    expected = 1736480 - ( -1042974 )
    assert expected == len(coords)
    subset_m_lenghts = [(1736480, 2000000), (-104297, 2000000)]
    fill_the_borders2(coords=coords, lens=subset_m_lenghts)
    assert expected == len(coords)
