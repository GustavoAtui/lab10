def contar_palavras(texto):
    contagem = {}
    for p in texto.split():
        contagem[p] = contagem.get(p, 0) + 1
    return contagem
