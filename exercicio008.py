# Exercicio 008 - Fatorial
# Faça um programa que leia um número inteiro e mostre na tela o seu fatorial, e assim com uma lista de multiplicações.

def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat

print(fatorial(4))

n = int(input("Digite um número: "))
for i in range(0, n + 1):
    print(f"{n} x {i} = {i * n}")
    
    