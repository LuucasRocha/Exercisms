#Mini calculadora
def main():
    calculadora(5, 2, "-")

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