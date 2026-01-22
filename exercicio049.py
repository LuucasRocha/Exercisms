#Gere uma lista de inteiros aleatórios e: quantas vezes o valor 9 aparece; em que posição está o valor 3; os valores pares.

import random

lista_aleatoria = [random.randint(1,10) for i in range(10)]

for num in lista_aleatoria:
    if 9 not in lista_aleatoria:
        contagem_nove = None
    else:
        contagem_nove = lista_aleatoria.count(9)

print(lista_aleatoria)

if contagem_nove:
    print(f"O valor 9 aparece {contagem_nove} vezes.")
else:
    print("O valor 9 não consta na lista.")
 
posicoes_3 = [i for i, num in enumerate(lista_aleatoria) if num == 3]

print(f"O valor 3 está nas posições {posicoes_3}.")

pares = list()
for num in lista_aleatoria:
    if num % 2 == 0:
        pares.append(num)

print(f"Pares: {pares}")
    

        
