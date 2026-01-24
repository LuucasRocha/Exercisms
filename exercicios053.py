# Faça um algoritmo que leia dois valores booleanos (lógicos) e determine se ambos são VERDADEIRO ou FALSO.

def verifica_booleano(a, b):
    if a and b == True:
        return True
    elif a and b == False:
        return False
    else:
        return None
    
valor_a = bool(input("Digite o primeiro valor: "))
valor_b = bool(input("Digite o segundo valor: "))

verificacao = verifica_booleano(valor_a, valor_b)

print(verificacao)

