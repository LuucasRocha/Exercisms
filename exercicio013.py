# Exercício 13
# Jogo de adivinhação
#Gere um número aleatório entre 1 e 100 e permita que o usuário tente adivinhar.
#Informe se o palpite é maior ou menor até acertar.

import random

num_aleatorio = random.randint(1, 100)

while True:
    palpite = int(input("Digite um palpite: "))
    if palpite == num_aleatorio:
        print("Parabéns, você acertou!")
        break
    elif palpite > num_aleatorio:
        print("O palpite foi maior que o número.")
    else:
        print("O palpite foi menor que o número.")
            
    
