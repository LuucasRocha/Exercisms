## Exercício 001 - Crie um programa que diga se denominada palavra é um palíndromo.

def palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()
    return palavra == palavra[::-1]

while True:
      entrada = input("Digite uma palavra(Ou 'sair' para encerrar o programa): ")
      if entrada.lower() == "sair":
          break
      if palindromo(entrada):
          print("A palavra é um palindromo.")
      else:
          print("A palavra não é um palindromo.")
