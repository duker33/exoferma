import typing as t
from attrs import define, field
from collections import namedtuple
from itertools import chain

from parsimonious.nodes import Node


@define
class ExoNode:
    """
    Node in terms of ExoFerma.

    Exists in two tree logics. Parser tree and Exo tree.
    """
    node: Node = field()

    @node.validator
    def check(self, attribute, value):
        if not isinstance(value, Node):
            raise TypeError(
                'ExoNode.node should be instance of parsimonious.Node.'
                f' Got type {type(value)}'
            )

    def has_expr(self, expr: str) -> bool:
        """Node has expression with given name among ancestors."""
        return expr in [en.node.expr_name for en in self.flatten()]

    def count_expr(self, expr: str) -> int:
        """Count has expressions with given name among the node ancestors."""
        return sum([int(en.node.expr_name == expr)  for en in self.flatten()])

    def flatten(self) -> t.List['ExoNode']:
        """Plain list of the node tree including itslef."""
        return (
            [self]
            + list(chain(*[ExoNode(n).flatten() for n in self.node.children]))
        )

    @property
    def children(self):
        return [ExoNode(n) for n in self.node.children]

    def flatten_exprs(self) -> t.List[str]:
        return [en.node.expr_name for en in self.flatten()]

    def find(self, expr_name: str) -> t.Union['ExoNode', None]:
        """Find in parser tree."""
        return next(
            (n for n in self.flatten() if n.node.expr_name == expr_name),
            None
        )

    def find_all(self, expr_name: str) -> t.List['ExoNode']:
        """Find all in parser tree."""
        return [n for n in self.flatten() if n.node.expr_name == expr_name]

    def _exo_leveled_lines(self) -> t.Union[t.List['ExoNode'], None]:
        if self.node.expr_name != 'paragraph':
            return
        ExoLine = namedtuple('ExoLine', ['level', 'content'])
        return [
            ExoLine(
                level=len(exo_line.find_all('line_indent')),
                content=exo_line.find('line_content')
            ) for exo_line in self.find_all('line')
        ]
