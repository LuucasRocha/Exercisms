"""Criar um programa que imprima todos os números inteiros de 1 até um limite definido pelo usuário."""

limite = int(input("Defina um limite superior: ")) 
lista_numeros = []

for i in range(1, limite + 1):
    lista_numeros.append(i)
    
print(f"Os números inteiros entre 1 e o limite superior definido é: {lista_numeros}")
print("Fim do programa.")




