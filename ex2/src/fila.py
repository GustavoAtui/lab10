class Fila:
    def __init__(self):
        self._num = {"normal": 0, "prioritaria": 0}
        self._senhas = []

    def emitir(self, tipo):
        if tipo not in self._num:
            raise ValueError("tipo invalido")
        self._num[tipo] += 1
        prefixo = "N" if tipo == "normal" else "P"
        senha = f"{prefixo}{self._num[tipo]}"
        self._senhas.append(senha)
        return senha

    @property
    def aguardando(self):
        return len(self._senhas)

    def chamar(self):
        if not self._senhas:
            raise IndexError("fila vazia")
        return self._senhas.pop(0)
