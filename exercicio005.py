#Criar um programa que converta uma temperatura de graus Celsius para Fahrenheit.

def conversor_temp(c):
    f = (c * 9/5) + 32
    return f

while True:
    print("***** Conversor de temperatura *****")
    c = float(input("Graus Célcius: "))
    print(f"{c} graus Célcius são {conversor_temp(c)} graus Farhenheit.")
    
    