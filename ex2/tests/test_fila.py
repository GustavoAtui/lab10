import pytest

from fila import Fila


def test_normal_vira_n1():
    assert Fila().emitir("normal") == "N1"


def test_numeracao_por_tipo():
    f = Fila()
    senhas = [f.emitir(t) for t in ["normal", "prioritaria", "normal", "prioritaria"]]
    assert senhas == ["N1", "P1", "N2", "P2"]


def test_tipo_invalido():
    with pytest.raises(ValueError):
        Fila().emitir("vip")


def test_aguardando():
    f = Fila()
    assert f.aguardando == 0
    f.emitir("normal")
    f.emitir("prioritaria")
    assert f.aguardando == 2


def test_chamar_vazia():
    with pytest.raises(IndexError):
        Fila().chamar()


def atender(tipos):
    f = Fila()
    for t in tipos:
        f.emitir(t)
    return [f.chamar() for _ in tipos]


def test_ordem_de_chegada():
    assert atender(["normal", "normal"]) == ["N1", "N2"]


def test_prioritaria_na_frente():
    assert atender(["normal", "prioritaria"]) == ["P1", "N1"]
