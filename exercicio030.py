# Exercicio 030
# Gere um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

numero_gerado = random.randint(0, 5)

while True: 
    
    numero_usuario = int(input("Adivinhe o número gerado: "))
    if numero_usuario == numero_gerado:
        print("Parabéns! Você venceu.")
        break
    else:
        print("Perdeu! Tente novamente.")

    