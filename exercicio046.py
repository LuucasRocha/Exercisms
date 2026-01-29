#Gere uma lista e diga quais foram os maiores valores e em quais posições da lista eles estão.

import random

lista_gerada = [random.randint(1, 20) for i in range(10)]

maior = 0
menor = 0

for i in lista_gerada:
    if i > maior:
        maior = i
    if i < menor or menor == 0:
        menor = i

print(f"Lista gerada: {lista_gerada}")
print(f"Maior valor: {maior} nas posições: ", end="")
for i in range(len(lista_gerada)):
    if lista_gerada[i] == maior:
        print(i, end=" ")
        
print(f"\nMenor valor: {menor} nas posições: ", end="")
for i in range(len(lista_gerada)):
    if lista_gerada[i] == menor:
        print(i, end=" ")   
        

        