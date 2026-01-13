cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

while True:
    try:
        entrada = int(input("Digite um número inteiro entre 0 e 20: "))
    except ValueError:
        print("Entrada inválida.", end=' ')
        continue
    
    if 20 > entrada > 0:
        print(f"Número {cont[entrada]}.")
    else:
        print("Erro. O número deve estar entre 0 e 20.")
        continue
    
    escolha = input("Deseja continuar? 's'/sim - 'n'/não")
    if escolha.lower() == 's':
        continue
    else:
        print("programa encerrado")
        break
        
         