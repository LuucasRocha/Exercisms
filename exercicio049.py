#Gere uma lista de inteiros aleatórios e: quantas vezes o valor 9 aparece; em que posição está o valor 3; os valores pares.
import random

lista_aleatoria = [random.randint(1,10) for i in range(10)]

for num in lista_aleatoria:
    if 9 in lista_aleatoria:
       contagem_nove = lista_aleatoria.count(9)
    else:
        contagem_nove = None

posicoes_3 = [i + 1 for i, num in enumerate(lista_aleatoria) if num == 3]

print(lista_aleatoria)
print(f"Contagem do valor 9: {contagem_nove}")
print(f"Posições do valor 3: {posicoes_3}")   


        
