'''
Implemente funções que:
Retornem maior, menor e média de uma lista
Contem números pares
Removam duplicados
Contem frequência de elementos
'''

def maior_elemento_lista(lista):
    return max(lista)

def menor_elemento_lista(lista):
    return min(lista)

def media_elementos_lista(lista):
    return sum(lista) / len(lista) if len(lista) != 0 else 0

def lista_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

def remover_duplicados(lista):
    nova_lista = []
    for num in lista:
        if num not in nova_lista:
            nova_lista.append(num)
    return nova_lista

def remover_duplicados_set(lista):
    return list(set(lista))

def remover_duplicados_set_com_ordem(lista):
    return list(dict.fromkeys(lista))

def frequencia_elementos(lista):
    frequencia = {}
    for numero in lista:
        if numero in frequencia:
            frequencia[numero] += 1
        else:
            frequencia[numero] = 1
    return frequencia 

lista_entrada = [5, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 1]







    

            

    
