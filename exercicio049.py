#Gere uma lista de inteiros aleatórios e: quantas vezes o valor 9 aparece; em que posição está o valor 3; os valores pares.

import random

lista_aleatoria = [random.randint(1, 10) for i in range(5)]

posicoes_3 = [i for i, num in enumerate(lista_aleatoria) if num == 3]

contagem_nove = lista_aleatoria.count(9)

print(lista_aleatoria)
print(contagem_nove)
print(posicoes_3)
        
