# Leia duas listas e crie uma terceira contendo somente os elementos que aparecem nas duas.
import random

lista1 = random.sample(range(1, 20), 10)
lista2 = random.sample(range(1, 20), 10)
print("Lista 1:", lista1)
print("Lista 2:", lista2)

nova_lista = []

for num in lista1:
    if num in lista2:
        nova_lista.append(num)

print("Elementos que aparecem nas duas listas:", nova_lista)
