#Gere uma lista e diga quais foram os maiores valores e em quais posições da lista eles estão.

import random

def posicoes_maiores_valores(lista):
    return [k for k, v in enumerate(lista) if v == max(lista)]

lista_gerada = [int(input("Digite um número inteiro: ")) for _ in range(10)]

print(f"Lista: {lista_gerada}")
print(f"Posições dos maiores valores: {posicoes_maiores_valores(lista_gerada)}")

