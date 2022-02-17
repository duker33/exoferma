from exoferma.parser import parse_file


def test_node_find():
    note = parse_file('tests/assets/node_find.xi')
    found = note.find('line')
    assert 'line' == found.node.expr_name
    assert 'one' in found.node.text


def test_node_find_chained():
    note = parse_file('tests/assets/node_find.xi')
    found = note.find('line').find('line_content')
    assert 'line_content' == found.node.expr_name
    assert found.node.text.endswith('one')


def test_node_find_all():
    note = parse_file('tests/assets/node_find.xi')
    found = note.find_all('line')
    assert 3 == len(found)
    should = ['one', 'two', 'three']
    for left, right in zip(should, found):
        assert left in right.node.text


def test_exo_leveled_lines_common():
    note = parse_file('tests/assets/node_simple.xi')
    xi_lines = note.find('paragraph')._exo_leveled_lines()
    first, second, third = xi_lines
    assert (0, '. one\n') == (first.level, first.exo_node.node.text)
    assert (1, '  . two\n') == (second.level, second.exo_node.node.text)
    assert (1, '  . three\n') == (third.level, third.exo_node.node.text)
    # .
    assert (0, 'one') == (
        first.level,
        first.exo_node.find('line').find('line_content').node.text
    )


def test_exo_leveled_lines_much_nesting():
    def content(xi_line):
        return xi_line.exo_node.find('line').find('line_content').node.text
    note = parse_file('tests/assets/node_much_nesting.xi')
    xi_lines = note.find('paragraph')._exo_leveled_lines()
    first, second, third, fourth, fifth = xi_lines
    assert (0, 'one') == (first.level, content(first))
    assert (1, 'two') == (second.level, content(second))
    assert (2, 'three') == (third.level, content(third))
    assert (2, 'four') == (fourth.level, content(fourth))
    assert (0, 'five') == (fifth.level, content(fifth))


def test_exo_leveled_lines_not_paragraph():
    note = parse_file('tests/assets/node_simple.xi')
    xi_lines = note.find('line')._exo_leveled_lines()
    assert xi_lines is None


def test_xi_children_common():
    note = parse_file('tests/assets/node_much_nesting.xi')
    paragraph = note.find('paragraph')
    children = paragraph.xi_children()
    for node in children:
        assert 'line' == node.node.expr_name
        assert node.parent == paragraph
    assert 2 == len(children), children
    assert '. one' == children[0].node.text.strip()
    assert '. five' == children[1].node.text.strip()


def test_xi_children_nested():
    note = parse_file('tests/assets/node_much_nesting.xi')
    paragraph = note.find('paragraph')
    node = paragraph
    for content in ['. one', '. two', '. three']:
        node = node.xi_children()[0]
        assert content == node.node.text.strip()
    # the leaf node has no children
    node = node.xi_children()[0]
    for node in node.xi_children():
        assert 'line' != node.node.expr_name
