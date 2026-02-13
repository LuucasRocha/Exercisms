#28. Escrever um algoritmo que lê a hora de início e hora de término de um jogo, 
#ambas subdivididas em dois valores distintos : horas e minutos. Calcular e escrever a duração do jogo,
# também em horas e minutos, considerando que o tempo máximo de duração de um jogo 
#é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.

def calcular_tempo_jogo(hora_inicio, hora_termino):
    # Converter horas e minutos para minutos totais
    inicio_total_minutos = hora_inicio[0] * 60 + hora_inicio[1]
    termino_total_minutos = hora_termino[0] * 60 + hora_termino[1]

    # Calcular a duração do jogo em minutos
    if termino_total_minutos >= inicio_total_minutos:
        duracao_minutos = termino_total_minutos - inicio_total_minutos
    else:
        duracao_minutos = (24 * 60 - inicio_total_minutos) + termino_total_minutos

    # Converter a duração de volta para horas e minutos
    duracao_horas = duracao_minutos // 60
    duracao_restante_minutos = duracao_minutos % 60

    return duracao_horas, duracao_restante_minutos



