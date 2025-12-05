"""Criar um programa que imprima todos os números inteiros de 1 até um limite definido pelo usuário."""

def imprimir_inteiros(n):
    limite = n
    for num in range(1, n + 1):
        print(num)

entrada = int(input("Digite um limite de inteiros: "))

imprimir_inteiros(entrada)



