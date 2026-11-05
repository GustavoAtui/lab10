import pytest

from contador import contar_palavras

CASOS = [
    ("", {}),
]


@pytest.mark.parametrize("texto, esp", CASOS)
def test_contar(texto, esp):
    assert contar_palavras(texto) == esp
