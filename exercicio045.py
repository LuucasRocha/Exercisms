cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

while True:
    try:
        entrada = int(input("Digite um número inteiro entre 0 e 20: "))
    except ValueError:
        print("Entrada inválida!", end=' ')
        continue
    
    if entrada < 0 or entrada > 20:
        print("Erro! O número inteiro deve estar entre 0 e 20.")
    else:
        print(f"O número digitado foi {cont[entrada]}")
        
    escolha = input("Digite 's' para continuar ou 'n' para encerrar: ")
    if escolha == 'N'.lower():
        print("Programa encerrado.")
        break
    else:
        continue