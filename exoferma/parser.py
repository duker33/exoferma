import typing as t

from parsimonious.grammar import Grammar
from parsimonious.nodes import Node

grammar = Grammar(
r"""
note = (paragraph / line_empty / emptyness)+
paragraph = (line / line_body)+

line_indent = "  "
line_head = ". "
line_end = ~"\n"
line_content = ~".*"
line_empty = line_indent* line_end
line_body = line_indent* line_head line_content
line = line_body line_end

emptyness = ""
"""
)

def fetch_text():
    with open('tests/assets/common_from.xi') as f:
        return f.read()

def parse(filename: str) -> Node:
    with open(filename) as f:
        return grammar.parse(f.read())
