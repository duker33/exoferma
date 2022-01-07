import pytest

from parsimonious.nodes import Node

from exoferma.nodes import ExoNode
from exoferma.parser import parse


# Have test here, because line is the most primitive abstraction
def test_empty_file():
    f = 'tests/assets/empty.xi'
    tree = parse(f)
    assert type(tree) == Node


def test_common_line():
    f = 'tests/assets/line_common.xi'
    note = parse(f)
    assert ExoNode(note).has_expr('line_body')
    assert not ExoNode(note).has_expr('line_empty')


def test_line_end():
    f = 'tests/assets/line_empty.xi'
    note = ExoNode(parse(f))
    assert note.has_expr('line_end')
    assert 1 == note.count_expr('line_end')
