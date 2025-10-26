#Crie uma função soma_pares(lista) que receba uma lista de números e retorne a soma somente dos pares

def soma_pares(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    return soma
            
lista = [1,2,3,4,5,6,7,8]
print(soma_pares(lista))