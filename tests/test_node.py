import pytest

from parsimonious.nodes import Node

from exoferma.nodes import ExoNode
from exoferma.parser import parse


def test_node_find():
    note = parse('tests/assets/node_find.xi')
    found = ExoNode(note).find('line')
    assert 'line' == found.node.expr_name
    assert 'one' in found.node.text
