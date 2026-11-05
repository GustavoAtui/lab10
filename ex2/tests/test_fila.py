import pytest

from fila import Fila


def test_normal_vira_n1():
    assert Fila().emitir("normal") == "N1"
