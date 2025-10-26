#Crie uma função analisa_lista(lista) que retorne o maior e o menor número contidos em uma lista de inteiros.

def analisa_lista(lista):
    return f"Maior: {max(lista)} | Menor: {min(lista)}"
'''
def analisa_lista(lista):
    maior = menor = lista[0]
    for num in lista:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    return f"Maior: {maior} | Menor: {menor}"
'''

lista = [1,2,3,4,5,6,7,8,9,10]
print(analisa_lista(lista))