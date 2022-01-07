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
    assert ExoNode(note).has_expr('line_last')
    assert 1 == ExoNode(note).count_expr('emptyline')

def test_empty_line():
    f = 'tests/assets/line_empty.xi'
    note = parse(f)
    assert ExoNode(note).has_expr('emptyline')
    assert 1 == ExoNode(note).count_expr('emptyline')
