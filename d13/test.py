from main import parse_packet


def test_parse_one_list():
    assert parse_packet('[]') == []
