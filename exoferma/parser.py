import typing as t

from exoferma.node import ExoNode

from parsimonious.grammar import Grammar
from parsimonious.nodes import Node

grammar = Grammar(
r"""
note = (paragraph / line_empty / emptyness)+
paragraph = (line / line_dot)+

line_indent = "  "
line_head = ". "
line_end = ~"\n"
line_content = ~".*"
line_empty = line_indent* line_end
line_dot = line_indent* line_head line_end
line = line_indent* line_head line_content line_end

emptyness = ""
"""
)

def normalize(text: str) -> str:
    return text.strip() + '\n'


def parse(text: str) -> ExoNode:
    return ExoNode(node=grammar.parse(normalize(text)))


def parse_file(filename: str) -> Node:
    with open(filename) as f:
        return parse(text=f.read())
