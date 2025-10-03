## Exercício 001 - Crie um programa que diga se denominada palavra é um palíndromo.

def eh_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1]

palavra = input("Digite uma palavra: ")
if eh_palindromo(palavra):
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")    
    
