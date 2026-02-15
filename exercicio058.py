#Mini calculadora
def main():
    calculadora(1, 1, "-")

def calculadora(x, y, operacao):
    if operacao == "+":
        print(x + y)
    elif operacao == "-":
        print(x - y)
    elif operacao == "*":
        print(x * y)
    elif operacao == "/":
        print(x / y)

main()