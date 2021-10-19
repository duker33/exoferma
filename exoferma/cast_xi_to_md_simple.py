def text():
    with open('common_from.xi') as f:
        return f.read()

def cast(source: str) -> str:
    return [cast_line(line) for line in source.split('\n')]

def cast_line(line: str) -> str:
    if line_is_heading(line):
        pass
    elif line_is_note(line):
        pass
    elif line_is_empty(line):
        pass
    else:
        raise ValueError(f'Unknown line type:\n{line}')

# <<
def line_is_heading(line: str) -> bool:
    pass

def line_is_note(line: str) -> bool:
    pass
# >>

def line_is_empty(line: str) -> bool:
    return not line.strip()

# <<
# def cast_(line: str) -> str:
#     pass

def cast_heading(line: str) -> str:
    pass

def cast_note(line: str) -> str:
    pass

def cast_link(chunk: str) -> str:
    pass
# >>

def main():
    return cast(text())


if __name__ == '__main__':
    print(main())
