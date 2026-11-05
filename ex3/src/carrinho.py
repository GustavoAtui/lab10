CUPONS = {"DEZ": 10}  # codigo -> porcentagem de desconto
MINIMOS = {"DEZ": 10000}  # codigo -> subtotal minimo


class Carrinho:
    def __init__(self):
        self._subtotal = 0
        self._cupom = None

    def adicionar(self, preco, quantidade=1):
        if preco <= 0:
            raise ValueError("preco deve ser positivo")
        self._subtotal += preco * quantidade

    def aplicar_cupom(self, codigo):
        if codigo not in CUPONS:
            raise ValueError("cupom desconhecido")
        self._cupom = codigo

    @property
    def total(self):
        desconto = 0
        if self._cupom and self._subtotal >= MINIMOS[self._cupom]:
            desconto = CUPONS[self._cupom]
        return self._subtotal * (100 - desconto) // 100
