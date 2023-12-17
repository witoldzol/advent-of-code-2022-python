from main import MAX_REGION
from main import merge_ranges


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
    # right extended multiple times and merge with last one
    new_range = (1,9)
    existing_range = [(1,2),(4,5),(10,12)]
    actual = merge_ranges(new_range, existing_range)
    assert  [(1,12)] == actual
    # right extended multiple times
    new_range = (0,10)
    existing_range = [(1,2),(4,5),(7,8)]
    actual = merge_ranges(new_range, existing_range)
    assert  [(0,10)] == actual
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
    # adjecent on the left
    new_range = (4,5)
    existing_range = [(6,8)]
    actual = merge_ranges(new_range, existing_range)
    assert  [(4,8)] == actual
    # adjecent on the right
    new_range = (3,4)
    existing_range = [(1,2),(6,8)]
    actual = merge_ranges(new_range, existing_range)
    assert  [(1,4),(6,8)] == actual
    # adjecent on both sides
    new_range = (3,4)
    existing_range = [(1,2),(5,8)]
    actual = merge_ranges(new_range, existing_range)
    assert  [(1,8)] == actual
    # single point join left & right
    new_range = (11,11)
    existing_range = [(1,10),(12,24)]
    actual = merge_ranges(new_range, existing_range)
    assert  [(1,24)] == actual
    # single point left bound
    new_range = (11,11)
    existing_range = [(-9,24)]
    actual = merge_ranges(new_range, existing_range)
    assert  [(-9,24)] == actual
    # single point left bound, multiple items
    new_range = (11,11)
    existing_range = [(1,7),(9,24)]
    actual = merge_ranges(new_range, existing_range)
    assert  [(1,7),(9,24)] == actual
    # 0,0
    new_range = (0,0)
    existing_range = [(1,7),(9,24)]
    actual = merge_ranges(new_range, existing_range)
    assert  [(0,7),(9,24)] == actual
    # inside
    new_range = (3,6)
    existing_range = [(1,7),(9,24)]
    actual = merge_ranges(new_range, existing_range)
    assert  [(1,7),(9,24)] == actual
    # inside
    new_range = (3,7)
    existing_range = [(1,7),(9,24)]
    # breakpoint()
    actual = merge_ranges(new_range, existing_range)
    assert  [(1,7),(9,24)] == actual



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
