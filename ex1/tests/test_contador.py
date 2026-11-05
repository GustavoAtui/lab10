import pytest

from contador import contar_palavras

CASOS = [
    ("", {}),
    ("teste", {"teste": 1}),
    ("bom dia", {"bom": 1, "dia": 1}),
]


@pytest.mark.parametrize("texto, esp", CASOS)
def test_contar(texto, esp):
    assert contar_palavras(texto) == esp
