# Implemente uma mini calculadora com funções: soma, subtração, multiplicação e divisão.
# O usuário escolhe a operação e os números. 

def calculadora(x, y, operacao):
    if operacao == '+':
        return x + y
    elif operacao == '-':
        return x - y
    elif operacao == '*':
        return x * y
    elif operacao == '/':
        return x / y
    else:
        return "Operação inválida"
    
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

resultado = calculadora(num1, num2, operacao)
print("Resultado:", resultado)