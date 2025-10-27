#Implemente mais_comum(lista) que retorna o elemento mais frequente da lista.
#Em caso de empate, retorne o que aparece primeiro na lista original.

from collections import Counter

def mais_comum(lista):
    if not lista:
        return "Lista vazia"
    cont = Counter(lista)
    mais_frequente = cont.most_common(1)[0][0]
    return mais_frequente

print(mais_comum([2,2,3,3,3,4,5,6]))  # → 3
print(mais_comum([]))                 # → "Lista vazia"
