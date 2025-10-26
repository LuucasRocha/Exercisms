## Exercício 001 - Crie um programa que diga se denominada palavra é um palíndromo.

def eh_palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()
    return palavra == palavra[::-1]

while True:
    
    entrada = input("Digite uma palavra: ")

    if eh_palindromo(entrada):
        print("A palavra digitada é um palíndromo.")
    else:
        print("A palavra digitada não é um palíndromo.")

