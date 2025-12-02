## Exercício 001 - Crie um programa que diga se denominada palavra é um palíndromo.

def eh_palindromo(palavra):
    palavra = palavra.lower()
    return palavra == palavra[::-1]

print(eh_palindromo(""))