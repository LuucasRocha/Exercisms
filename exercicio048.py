import random

numeros_sorteados = tuple(random.randint(1, 5) for i in range(5))

print(numeros_sorteados)

def maior_menor(tupla):
    maior = max(tupla)
    menor = min(tupla)
    return f"Maior: {maior}\nMenor: {menor}"

print(maior_menor(numeros_sorteados))