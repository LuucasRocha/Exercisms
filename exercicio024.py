#Crie uma função conta_pares_impares(lista) que receba uma lista de números e retorne quantos pares e quantos ímpares ela tem.

def conta_pares_impares(lista):
    pares = [num for num in lista if num % 2 == 0]
    impares = sum(1 for num in lista if num % 2 != 0)
    
    return len(pares), impares

print(conta_pares_impares([]))