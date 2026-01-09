def frequencia(lista):
    frequencia = {}
    
    for numero in lista:
        frequencia[numero] = frequencia.get(numero, 0) + 1
    
    return frequencia

lista_entrada = [4, 80, 6, 6, 34, 20, 2, 2]
print(frequencia(lista_entrada))

def remover_duplicados(lista):
   return list(dict.fromkeys(lista))

def remover_duplicados_set(lista):
    return list(set(lista))

print(remover_duplicados_set(lista_entrada))
sem_duplicados = remover_duplicados(lista_entrada)
print( sem_duplicados)