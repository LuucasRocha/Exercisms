#Remova duplicados

def remover_duplicados(lista):
    nova_lista = []
    
    for i in lista:
        if i not in nova_lista:
            nova_lista.append(i)
    
    return nova_lista

print(remover_duplicados([2,3,4,4,5,6,7,7,8]))