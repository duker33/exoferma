from parsimonious.grammar import Grammar

# grammar = Grammar(
# r"""
# block = sentence*
# sentence = ". " line eol
# eol = ~"\n"
# line = ~"[.*]"i
# """
# )

grammar = Grammar(
r"""
xi_node = (xi_node / line / emptyline)*
line = some_space ". " ~".*" eol
eol = ~"\n"
some_space = ~"\s*"
emptyline = ~"some_space+"
"""
)

def text():
    with open('morpher_from.xi') as f:
        return f.read()

def main():
    return grammar.parse(text())


if __name__ == '__main__':
    print(main())
