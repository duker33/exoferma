import typing as t
from attrs import define, field
from collections import defaultdict, namedtuple
from itertools import chain

from parsimonious.nodes import Node


@define
class ExoNode:
    """
    Node in terms of ExoFerma.

    Exists in two tree logics. Parser tree and Exo tree.
    """
    node: Node = field()
    parent: t.Union['ExoNode', None] = field(default=None)
    xi_children_field: t.List['ExoNode'] = field(factory=list)
    FIELDS = ['node', 'parent', 'xi_children_field']

    @node.validator
    def check(self, attribute, value):
        if not isinstance(value, Node):
            raise TypeError(
                'ExoNode.node should be instance of parsimonious.Node.'
                f' Got type {type(value)}'
            )

    def copy(self, **kwargs) -> 'ExoNode':
        n = getattr(self, 'node')
        return ExoNode(
            **{f: kwargs.get(f, getattr(self, f)) for f in ExoNode.FIELDS}
        )

    def __str__(self) -> str:
        return self.node.text.strip()

    def __repr__(self) -> str:
        return self.node.text.strip()

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
    def children(self) -> t.List['ExoNode']:
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
        ExoLine = namedtuple('ExoLine', ['level', 'exo_node'])
        return [
            ExoLine(
                level=len(exo_line.find_all('line_indent')),
                exo_node=exo_line,
            ) for exo_line in self.find_all('line')
        ]

    def xi_children(self) -> t.List['ExoNode']:
        """Children in terms of XI Exo tree, but not parser tree."""
        if self.node.expr_name == 'paragraph':
            xi_lines = self._exo_leveled_lines()
            lines_by_level = defaultdict(list)
            for line in xi_lines:
                if line.level > 0:
                    parent = lines_by_level[line.level - 1].pop()
                    exo_line = line.exo_node
                    exo_line.parent = parent
                    parent.xi_children_field.append(exo_line)
                    lines_by_level[line.level - 1].append(parent)
                    lines_by_level[line.level].append(exo_line)
                else:
                    assert line.level == 0
                    lines_by_level[line.level].append(
                        line.exo_node.copy(parent=self)
                    )
            return lines_by_level.get(0, [])
        else:
            return self.xi_children_field or self.children
