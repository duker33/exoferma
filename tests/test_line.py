from exoferma.node import ExoNode
from exoferma.parser import parse_file


# Have test here, because line is the most primitive abstraction
def test_empty_file():
    tree = parse_file('tests/assets/empty.xi')
    assert type(tree) == ExoNode


def test_common_line():
    note = parse_file('tests/assets/line_common.xi')
    assert note.has_expr('line')
    assert not note.has_expr('line_empty')


def test_line_end():
    note = parse_file('tests/assets/line_empty.xi')
    assert note.has_expr('line_end')
    assert 1 == note.count_expr('line_end')
