# Exercício 17
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.

nome_completo = input("Digite seu nome completo: ")
print("Nome em maiúsculas:", nome_completo.upper())
print("Nome em minúsculas:", nome_completo.lower())
# - Quantas letras ao todo (sem considerar espaços).
letras_sem_espacos = len(nome_completo.replace(" ", ""))
print("Total de letras (sem espaços):", letras_sem_espacos)