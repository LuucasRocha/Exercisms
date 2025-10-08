# Exercicio 008 - Fatorial
# Faça um programa que leia um número inteiro e mostre na tela o seu fatorial, e assim com uma lista de multiplicações.

n = int(input("Digite um número inteiro: "))
fatorial = 1
for i in range(1, n + 1):
    fatorial *= i
print("O fatorial de", n, "é", fatorial)

print("Lista de multiplicações:")
for i in range(1, n + 1):
    print(n, "x", i, "=", n * i)
    
    