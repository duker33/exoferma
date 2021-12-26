from parsimonious.grammar import Grammar

# grammar = Grammar(
# r"""
# block = sentence*
# sentence = ". " line eol
# eol = ~"\n"
# line = ~"[.*]"i
# """
# )

# grammar = Grammar(
# r"""
# xi_node = (xi_node / line / emptyline)*
# line = some_space ". " ~".*" eol
# eol = ~"\n"
# some_space = ~"\s*"
# emptyline = ~"some_space+"
# """
# )

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

def main():
    return grammar.parse(fetch_text())


if __name__ == '__main__':
    print(main())
