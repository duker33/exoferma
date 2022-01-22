import pytest

from parsimonious.nodes import Node

from exoferma.node import ExoNode
from exoferma.parser import parse


def test_paragraph():
    f = 'tests/assets/paragraph.xi'
    note = parse(f)
    assert ExoNode(note).has_expr('paragraph')
    assert 1 == ExoNode(note).count_expr('paragraph')


def test_paragraphs():
    f = 'tests/assets/paragraphs.xi'
    note = parse(f)
    assert 2 == ExoNode(note).count_expr('paragraph')
