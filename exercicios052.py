#Gere lista aleatoria e remova os duplicados e mostre a frequencia de cada elemento.

import random

lista_aleatoria = [random.randint(1, 10) for i in range(15)]

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

print(f"Lista aleatória: {lista_aleatoria}")
print(f"Lista sem duplicados: {remover_duplicados(lista_aleatoria)}")
print(f"Frequência de cada elemento: {frequencia_elemento(lista_aleatoria)}")