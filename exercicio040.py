'''
Implemente funções que:
Analisem se um número é:
positivo, negativo ou zero
Retornem o maior entre dois números
Classifiquem um triângulo (inválido, equilátero, isósceles, escaleno)
Verifiquem se um número é primo
'''

def analisa_numero(num):
    if num == 0:
        return "Zero"
    elif num < 0:
        return "Negativo"
    else:
        return "Positivo"

def retorna_maior(num1, num2):
    if num1 == num2:
        return "Números iguais."
    else:
        return num1 if num1 > num2 else num2
    
def classifica_triangulo(num1, num2, num3):
    if num1 < (num2 + num3) and num2 < (num1 + num3) and num3 < (num1 + num2):
        if num1 == num2 and num1 == num3 and num2 == num3:
            return "Equilátero"
        elif num1 == num2 or num1 == num3 or num2 == num3:
            return "Isósceles"
        elif num1 != num2 and num1 != num3 and num2 != num3:
            return "Escaleno"
    else:
        return "Não é possível formar triângulo."

def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True




