def contar_palavras(texto):
    contagem = {}
    for p in texto.lower().split():
        p = p.strip(".,;:!?")
        if p:
            contagem[p] = contagem.get(p, 0) + 1
    return contagem
