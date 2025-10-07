# Faça um algoritmo que receba um valor inteiro e imprima na tela a sua tabuada.

def tab_num(num):
    return f"{num} * 1 = {num * 1}\n{num} * 2 = {num * 2}\n{num} * 3 = {num * 3}\n{num} * 4 = {num * 4}\n{num} * 5 = {num * 5}\n{num} * 6 = {num * 6}\n{num} * 7 = {num * 7}\n{num} * 8 = {num * 8}\n{num} * 9 = {num * 9}\n{num} * 10 = {num * 10}\n"

valor = int(input("Digite um valor inteiro: "))
print(f"A tabuada de {valor} é: ")
print(tab_num(valor))