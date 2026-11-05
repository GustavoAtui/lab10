class Fila:
    def __init__(self):
        self._num = {"normal": 0, "prioritaria": 0}

    def emitir(self, tipo):
        if tipo not in self._num:
            raise ValueError("tipo invalido")
        self._num[tipo] += 1
        prefixo = "N" if tipo == "normal" else "P"
        return f"{prefixo}{self._num[tipo]}"
