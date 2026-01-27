#Gere lista aleatoria e remova os duplicados e mostre a frequencia de cada elemento.

import random

def remover_duplicados(lista):
    return list(dict.fromkeys(lista))

def frequencia_elemento(lista):
    frequencia = dict()
    
    for numero in lista:
        if numero not in frequencia:
            frequencia[numero] = 1
        else:
            frequencia[numero] += 1 
    
    return frequencia   

lista_aleatoria = list(random.randint(1, 10) for i in range(10))
lista_sem_duplicados = remover_duplicados(lista_aleatoria)
lista_frequencia = frequencia_elemento(lista_aleatoria)

print(f"Lista gerada: {lista_aleatoria}")
print(f"Lista sem duplicados: {lista_sem_duplicados}")
print(f"Frequência dos elementos da lista: {lista_frequencia}")


