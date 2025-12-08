# Leia duas listas e crie uma terceira contendo somente os elementos que aparecem nas duas.

import random

primeira_lista = [random.randint(1, 10) for _ in range(10)]
segunda_lista = [random.randint(1, 10) for _ in range(10)]

terceira_lista = list(set(primeira_lista) and set(segunda_lista))

print(primeira_lista)
print(segunda_lista)
print(terceira_lista)
