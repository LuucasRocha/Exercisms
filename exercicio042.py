'''
Implemente funções que:
Retornem maior, menor e média de uma lista
Contem números pares
Removam duplicados
Contem frequência de elementos
'''

def maior_elemento(lista):
    maior = lista[0]
    
    for numero in lista:
        if numero > maior:
            maior = numero
    
    return maior

def menor_elemento(lista):
    return min(lista)

def media_lista(lista):
    if len(lista) > 0:
        return sum(lista) / len(lista)
    else:
        return None

def remover_duplicados(lista):
    return list(set(lista))

def frequencia_elementos(lista):
    frequencia = dict()
    
    for numero in lista:
        if numero not in frequencia:
            frequencia[numero] = 1
        else:
            frequencia[numero] += 1
    
    return frequencia

lista_entrada = []










    

            

    
