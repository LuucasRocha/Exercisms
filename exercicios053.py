# Faça um algoritmo que leia dois valores booleanos (lógicos) e determine se ambos são VERDADEIRO ou FALSO.

def determina_booleanos(x1, x2):
    if x1 == True and x2 == True:
        return "Verdadeiro"
    elif x1 == False and x2 == False:
        return "Falso"
    elif x1 != x2:
        return "Diferente"

print(determina_booleanos(False, False))