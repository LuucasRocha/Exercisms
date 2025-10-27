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

entrada = input("Digite uma lista de números separados por espaço.")

lista = [int(x) for x in entrada.split()]
analise = analisa_lista(lista)

print(analise)