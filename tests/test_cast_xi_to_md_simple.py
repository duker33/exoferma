import pytest

from exoferma import cast_xi_to_md_simple as cs

ASSETS_BASE = 'tests/assets'


def test_cast() -> str:
    pass
    with open(f'{ASSETS_BASE}/common_from.xi') as f:
        l_from = f.read()
    with open(f'{ASSETS_BASE}/common_to.xi') as f:
        l_to = f.read()
    assert cs.cast(l_from) == l_to

# <<
def test_line_is_heading() -> bool:
    f = cs.line_is_heading
    assert f('Heading .')
    assert not f('. Note, but not Heading .')
    assert f('  Heading .  ')
    assert f('Heading . .')
    assert not f('Not Heading')
    assert not f('Not Heading too.')
    assert not f('')

def test_line_is_note() -> bool:
    f = cs.line_is_note
    assert f('. Note')
    assert f('  . Note')
    assert f('. . Note')
    assert f('. Note, but not Heading .')
    assert not f('Not Note')
    assert not f('Not Note too.')
    assert not f('')
    assert f('.')
    assert f('  .')
    assert f('.  ')
    assert f('  .  ')
# >>

def test_line_is_empty() -> bool:
    pass

# <<
# def test_cast_() -> str:
#     pass

def test_cast_heading() -> str:
    f = cs.cast_heading
    assert f('One .') == '**One**'
    with pytest.raises(AssertionError):
        f('One')
    with pytest.raises(AssertionError):
        f('. One .')

def test_cast_note() -> str:
    f = cs.cast_note
    assert f('. One') == '- One'
    with pytest.raises(AssertionError):
        f('One')
    assert f('. One .') == '- One .'

def test_cast_link() -> str:
    pass
# >>
