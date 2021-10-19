import exoferma as ef


def test_cast(source: str) -> str:
    pass

def test_cast_line(line: str) -> str:
    pass

# <<
def test_line_is_heading(line: str) -> bool:
    pass

def test_line_is_note(line: str) -> bool:
    pass
# >>

def test_line_is_empty(line: str) -> bool:
    return not line.strip()

# <<
# def test_cast_(line: str) -> str:
#     pass

def test_cast_heading(line: str) -> str:
    pass

def test_cast_note(line: str) -> str:
    pass

def test_cast_link(chunk: str) -> str:
    pass
# >>
