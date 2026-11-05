Exercício 1

a) Ordem: "", "teste", "bom dia", "dia a dia", "Dia dia DIA", "fim.   Fim!", três espaços, "bom\ndia", "guarda-chuva", ",dia, ;dia;", ":dia:  ?dia?", "... !". O "" vem primeiro porque só exige que a função exista e devolva um dict. O "teste" vem depois porque obriga a contar uma palavra.

c)
```
bc6f9e7 RED: texto vazio devolve dicionario vazio
d8d7e78 GREEN: texto vazio devolve dicionario vazio
f3c7200 RED: uma palavra conta 1
3a2bba7 GREEN: uma palavra conta 1
47d1fa2 RED: espaco separa duas palavras
c0f5522 GREEN: espaco separa duas palavras
608be2d RED: palavra repetida soma ocorrencias
93b0de7 GREEN: palavra repetida soma ocorrencias
4c141f3 RED: maiusculas contam como minusculas
b823ed1 GREEN: maiusculas contam como minusculas
500a0b5 RED: sinais nas bordas sao ignorados
78a718c GREEN: sinais nas bordas sao ignorados
30048f8 REFACTOR: testes que passaram de primeira documentam o contrato
18227e1 RED: palavra so de sinais e descartada
67bf97a GREEN: palavra so de sinais e descartada
```
Nenhum GREEN veio sem RED antes.

d) Três espaços, "bom\ndia" e "guarda-chuva" passaram porque o split() já tratava. ",dia, ;dia;" e ":dia:  ?dia?" passaram porque o strip() já tratava. Ficam na suíte, porque documentam o contrato.

e) 100% de ramos. 13 mutantes, 12 mortos. O vivo troca o strip por "XX.,;:!?XX" e é equivalente, porque o texto já passou por lower(). MS = 12/12 = 100%.

Exercício 2

a) N1 na primeira normal; numeração por tipo (N1, P1, N2, P2); tipo inválido dá ValueError; aguardando conta as emitidas; fila vazia dá IndexError; ordem de chegada (N1, N2); prioritária na frente (P1, N1); normal depois de 2 prioritárias (P1, P2, N1, P3); contagem zera (P1, P2, N1, P3, P4, N2); sem normal o limite não vale (P1, P2, P3).

c) Contar: test_normal_depois_de_duas_prioritarias. Zerar: test_contagem_zera_apos_normal.

d) test_sem_normal_limite_nao_vale.

e) 55 mutantes, 49 mortos (MS = 89%). Os 6 vivos são mensagens de erro, que a especificação não define, então não indicam regra sem teste. Mas o mutmut não muta @property, e nenhum teste confere aguardando depois de chamar().

Exercício 3

a) test_cupom (5000 dava 4500, agora fica 5000) e test_item_apos_cupom (900, agora 1000). Antes de mudar o código, reescrevi os dois com o valor novo (RED).

c) Os 17 testes continuam passando sem mudar nenhum.

d) 0 (abaixo do mínimo), 1 (o mínimo), 2 (já existia) e 1.5 (não inteira).
