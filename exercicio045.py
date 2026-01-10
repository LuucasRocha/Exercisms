cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

while True:
    try:
        entrada = int(input("Digite um número entre 0 e 20: "))
    except ValueError:
        print("Entrada inválida. ", end='')
        continue 
    
    if entrada > 20 or entrada < 0:
        print("Apenas números entre 0 e 20")
    else:
        print(f"Você digitou o número {cont[entrada]}")
  