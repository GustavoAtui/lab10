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
        normais, prioritarias = self._filas["normal"], self._filas["prioritaria"]
        if normais and (self._seguidas >= 2 or not prioritarias):
            self._seguidas = 0
            return normais.pop(0)
        if prioritarias:
            self._seguidas += 1
            return prioritarias.pop(0)
        raise IndexError("fila vazia")
