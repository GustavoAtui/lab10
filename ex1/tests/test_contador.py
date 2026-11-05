import pytest

from contador import contar_palavras

CASOS = [
    ("", {}),
    ("teste", {"teste": 1}),
    ("bom dia", {"bom": 1, "dia": 1}),
    ("dia a dia", {"dia": 2, "a": 1}),
    ("Dia dia DIA", {"dia": 3}),
    ("fim.   Fim!", {"fim": 2}),
    ("bom   dia", {"bom": 1, "dia": 1}),
    ("bom\ndia", {"bom": 1, "dia": 1}),
    ("guarda-chuva", {"guarda-chuva": 1}),
    (",dia, ;dia;", {"dia": 2}),
    (":dia:  ?dia?", {"dia": 2}),
    ("... !", {}),
]


@pytest.mark.parametrize("texto, esp", CASOS)
def test_contar(texto, esp):
    assert contar_palavras(texto) == esp
