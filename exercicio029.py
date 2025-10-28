#Implemente mais_comum(lista) que retorna o elemento mais frequente da lista.
#Em caso de empate, retorne o que aparece primeiro na lista original.

from collections import Counter

def mais_comum(lista):
    if not lista:
        return "Lista vazia."
    cont = Counter(lista)
    mais_comum = max(cont.values())
    for item in lista:
        if cont[item] == mais_comum:
            return item

entrada = input("Digite uma lista de números separados por espaço: ")

lista_numeros = [int(x) for x in entrada.split()]

print(f"Número mais frequente da lista: {mais_comum(lista_numeros)}")
    