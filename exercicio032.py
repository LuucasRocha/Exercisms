#exercicio 32 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input("Digite um número inteiro: "))

if numero < 2:
    print(f"{numero} não é um número primo.")   
else:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print(f"{numero} não é um número primo.")
            break
    else:
        print(f"{numero} é um número primo.")

