import pytest

from carrinho import Carrinho


def test_vazio():
    assert Carrinho().total == 0


def test_um_item():
    c = Carrinho()
    c.adicionar(2500)
    assert c.total == 2500


def test_quantidade():
    c = Carrinho()
    c.adicionar(2500, quantidade=2)
    assert c.total == 5000


def test_preco_zero():
    with pytest.raises(ValueError):
        Carrinho().adicionar(0)


def com_cupom(subtotal, *cupons):
    c = Carrinho()
    c.adicionar(subtotal)
    for codigo in cupons:
        c.aplicar_cupom(codigo)
    return c.total


@pytest.mark.parametrize(
    "subtotal, esp",
    [(5000, 5000), (9999, 9999), (10000, 9000)],
)
def test_dez(subtotal, esp):
    assert com_cupom(subtotal, "DEZ") == esp


@pytest.mark.parametrize(
    "subtotal, esp",
    [(29999, 29999), (30000, 24000)],
)
def test_vinte(subtotal, esp):
    assert com_cupom(subtotal, "VINTE") == esp


def test_cupom_desconhecido():
    with pytest.raises(ValueError):
        Carrinho().aplicar_cupom("XYZ")


def test_item_apos_cupom():
    c = Carrinho()
    c.aplicar_cupom("DEZ")
    c.adicionar(1000)
    assert c.total == 1000


def test_cupom_vale_ao_chegar_no_minimo():
    c = Carrinho()
    c.adicionar(5000)
    c.aplicar_cupom("DEZ")
    c.adicionar(5000)
    assert c.total == 9000
