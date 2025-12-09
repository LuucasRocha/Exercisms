# Exercicio 030
# Gere um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random 

gerador = random.randint(0, 5) 

while True:
    entrada = int(input("Chute um número de 0 a 5: ")) 
    if entrada != gerador:
        print("Perdeu")
    else:
        print("Venceu")
        break