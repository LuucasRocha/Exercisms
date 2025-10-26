#Crie uma função conta_pares_impares(lista) que receba uma lista de números e retorne quantos pares e quantos ímpares ela tem.

def conta_pares_impares(lista):
    pares = 0
    impares = 0
    for num in lista:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    return f"Pares: {pares} | Ímpares: {impares}"


'''def conta_pares_impares(lista):
    pares = sum(1 for num in lista if num % 2 == 0)
    impares = len(lista) - pares
    return f"Pares: {pares} | Ímpares: {impares}"
'''

lista_entrada = [1,2,3,4,5,6,7,8,9,10]
print(conta_pares_impares(lista_entrada))

