import random
#exercicio 32 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

def eh_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Retorne quantos elementos em uma lista são primos.
lista = [random.randint(1, 10) for _ in range(10)]

cont_primo = 0
for n in lista:
    if eh_primo(n):
        cont_primo += 1
        
print(lista)
print(cont_primo)



