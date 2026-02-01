#6. Faça um algoritmo que leia o tempo de duração de um evento em uma fábrica expressa em segundos e mostre-o expresso em horas, minutos e segundos.

import random

def converter_tempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    
    return horas, minutos, segundos_restantes

tempo_aleatorio = random.randint(1, 10000)
conversao = converter_tempo(tempo_aleatorio)

print(f"Tempo em segundos: {tempo_aleatorio}")
print(f"Convertido: {conversao[0]} horas, {conversao[1]} minutos e {conversao[2]} segundos")



        