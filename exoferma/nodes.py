import typing as t
from attrs import define
from itertools import chain

from parsimonious.nodes import Node


@define
class ExoNode:
    """Node in terms of ExoFerma."""
    node: Node

    def has_expr(self, expr: str) -> bool:
        """Node has expression with given name among ancestors."""
        return expr in [en.node.expr_name for en in self.flatten()]

    def count_expr(self, expr: str) -> int:
        """Count has expressions with given name among the node ancestors."""
        return sum([int(en.node.expr_name == expr)  for en in self.flatten()])

    def flatten(self) -> t.List[Node]:
        """Plain list of the node tree including itslef."""
        return (
            [self]
            + list(chain(*[ExoNode(n).flatten() for n in self.node.children]))
        )
