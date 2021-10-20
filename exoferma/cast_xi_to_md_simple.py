def text():
    with open('common_from.xi') as f:
        return f.read()

def cast(source: str) -> str:
    return '\n'.join([cast_line(line) for line in source.split('\n')])

def cast_line(line: str) -> str:
    ll = line
    if line_is_heading(ll):
        ll = cast_heading(ll)
    elif line_is_note(ll):
        ll = cast_note(ll)
    elif line_is_code(ll):
        pass
    elif line_is_empty(ll):
        pass
    else:
        raise ValueError(f'Unknown line type:\n{line}')
    return ll

# <<
def line_is_heading(line: str) -> bool:
    return (
        line.strip().endswith(' .')
        and not line_is_note(line)
        and not line_is_code(line)
    )

def line_is_note(line: str) -> bool:
    ll = line.strip()
    return ll == '.' or ll.startswith('. ')

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

def cast_note(line: str) -> str:
    assert line_is_note(line)
    indent = take_left_indent(line)
    return f'{indent}- {line.lstrip()[2:]}'.rstrip()

def cast_link(chunk: str) -> str:
    pass

def take_left_indent(line: str) -> str:
    return line[:len(line)-len(line.lstrip())]
# >>

def main():
    return cast(text())


if __name__ == '__main__':
    print(main())
