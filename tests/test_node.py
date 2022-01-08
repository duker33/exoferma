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
