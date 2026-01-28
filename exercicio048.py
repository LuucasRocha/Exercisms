#Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente.

def imprimir_decrescente(num1, num2, num3):
    numeros = [num1, num2, num3]
    return sorted(numeros, reverse=True)
    
print(imprimir_decrescente(3, 10, 3553))