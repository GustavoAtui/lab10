class Fila:
    def __init__(self):
        self._num = {"normal": 0, "prioritaria": 0}
        self._filas = {"normal": [], "prioritaria": []}
        self._seguidas = 0

    def emitir(self, tipo):
        if tipo not in self._num:
            raise ValueError("tipo invalido")
        self._num[tipo] += 1
        prefixo = "N" if tipo == "normal" else "P"
        senha = f"{prefixo}{self._num[tipo]}"
        self._filas[tipo].append(senha)
        return senha

    @property
    def aguardando(self):
        return len(self._filas["normal"]) + len(self._filas["prioritaria"])

    def chamar(self):
        if self._filas["prioritaria"] and not (self._seguidas >= 2 and self._filas["normal"]):
            self._seguidas += 1
            return self._filas["prioritaria"].pop(0)
        if self._filas["normal"]:
            self._seguidas = 0
            return self._filas["normal"].pop(0)
        raise IndexError("fila vazia")
