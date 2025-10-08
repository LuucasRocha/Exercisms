# Exercicio 009 - Fibonacci
# Faça um programa que leia um número inteiro e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.

n = int(input("Digite um número inteiro: "))
fibonacci = [0, 1]
for i in range(2, n):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
print("Os primeiros", n, "elementos da sequência de Fibonacci são:", fibonacci[:n])

