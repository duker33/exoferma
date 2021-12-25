import argparse


def cast(source: str) -> str:
    return '\n'.join([cast_line(line) for line in source.split('\n')])

def cast_line(line: str) -> str:
    ll = line
    if line_is_heading(ll):
        ll = cast_heading(ll)
    elif line_is_sentence(ll):
        ll = cast_sentence(ll)
    elif line_is_note(ll):
        ll = cast_note(ll)
    elif line_is_code(ll):
        pass
    elif line_is_empty(ll):
        pass
    else:
        pass
    return ll

# <<
def line_is_heading(line: str) -> bool:
    return (
        line.strip().endswith(' .')
        and not line_is_sentence(line)
        and not line_is_code(line)
    )

def line_is_sentence(line: str) -> bool:
    ll = line.strip()
    return ll == '.' or ll.startswith('. ')

def line_is_note(line: str) -> bool:
    ll = line.strip()
    return ll == '!' or ll.startswith('! ')

def line_is_code(line: str) -> bool:
    return line.strip().startswith('| ')
# >>

def line_is_empty(line: str) -> bool:
    return not line.strip()

# <<
# def cast_(line: str) -> str:
#     pass

def cast_heading(line: str) -> str:
    assert line_is_heading(line)
    indent = take_left_indent(line)
    return f'{indent}**{line.strip().rstrip()[:-2]}**'

def cast_sentence(line: str) -> str:
    assert line_is_sentence(line)
    indent = take_left_indent(line)
    return f'{indent}- {line.lstrip()[2:]}'.rstrip()

def cast_note(line: str) -> str:
    assert line_is_note(line)
    indent = take_left_indent(line)
    return f'{indent}- {line.lstrip()[2:]}'.rstrip()

def cast_link(chunk: str) -> str:
    pass

def take_left_indent(line: str) -> str:
    return line[:len(line)-len(line.lstrip())]
# >>

def main(args):
    file_from, file_to = args.from_to
    with open(file_from) as f:
        text_from = f.read()
    text_to = cast(text_from)
    with open(file_to, 'w') as f:
        f.write(text_to)

def _args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'from_to', type=str, nargs=2,
        help='File to read from and file to write from'
    )
    return parser.parse_args()

if __name__ == '__main__':
    main(_args())
