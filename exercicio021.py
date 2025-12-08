#Crie uma função soma_pares(lista) que receba uma lista de números e retorne a soma somente dos pares

def somaPares(lista):
    lista_pares = []
    for num in lista:
        if num % 2 == 0:
            lista_pares.append(num)
    return sum(lista_pares)

entrada = [1, 2, 3, 4, 5, 6, 7, 8]

print(somaPares(entrada))
