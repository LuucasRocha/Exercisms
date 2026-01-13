def frequencia_numero(lista):
    frequencia = {}
    
    for numero in lista:
        if numero in frequencia:
            frequencia[numero] += 1
        
        else:
            frequencia[numero] = 1
            
    return frequencia

lista = [3, 3, 4, 5, 5, 5, 6, 7, 7, 7, 7, 7, 8, 9]
print(frequencia_numero(lista))