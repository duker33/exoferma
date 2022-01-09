import pytest

from parsimonious.nodes import Node

from exoferma.nodes import ExoNode
from exoferma.parser import parse


def test_node_find():
    note = parse('tests/assets/node_find.xi')
    found = ExoNode(note).find('line')
    assert 'line' == found.node.expr_name
    assert 'one' in found.node.text


def test_node_find_chained():
    note = parse('tests/assets/node_find.xi')
    found = ExoNode(note).find('line').find('line_body')
    assert 'line_body' == found.node.expr_name
    assert found.node.text.endswith('one')


def test_node_find_all():
    note = parse('tests/assets/node_find.xi')
    found = ExoNode(note).find_all('line')
    assert 3 == len(found)
    should = ['one', 'two', 'three']
    for left, right in zip(should, found):
        assert left in right.node.text


def test_node_find_all_empty():
    note = parse('tests/assets/node_find.xi')
    found = ExoNode(note).find('line_body').find_all('line')
    assert not found


def test_exo_leveled_lines_common():
    note = parse('tests/assets/node_simple.xi')
    xi_lines = ExoNode(note).find('paragraph')._exo_leveled_lines()
    first, second, third = xi_lines
    assert (0, 'one') == (first.level, first.content.node.text)
    assert (1, 'two') == (second.level, second.content.node.text)
    assert (1, 'three') == (third.level, third.content.node.text)


def test_exo_leveled_lines_much_nesting():
    note = parse('tests/assets/node_much_nesting.xi')
    xi_lines = ExoNode(note).find('paragraph')._exo_leveled_lines()
    first, second, third, fourth, fifth = xi_lines
    assert (0, 'one') == (first.level, first.content.node.text)
    assert (1, 'two') == (second.level, second.content.node.text)
    assert (2, 'three') == (third.level, third.content.node.text)
    assert (2, 'four') == (fourth.level, fourth.content.node.text)
    assert (0, 'five') == (fifth.level, fifth.content.node.text)

def test_exo_leveled_lines_not_paragraph():
    note = parse('tests/assets/node_simple.xi')
    xi_lines = ExoNode(note).find('line')._exo_leveled_lines()
    assert xi_lines is None
