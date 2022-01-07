import typing as t

from parsimonious.grammar import Grammar
from parsimonious.nodes import Node

grammar = Grammar(
r"""
note = (paragraph / emptyline)+
paragraph = (line / line_last)+

line_last = ". " ~".*"
line = line_last eol
eol = ~"\n"

emptyline = (some_space / eol)*
some_space = ~"\s*"
"""
)

def fetch_text():
    with open('tests/assets/common_from.xi') as f:
        return f.read()

def parse(filename: str) -> Node:
    with open(filename) as f:
        return grammar.parse(f.read())
