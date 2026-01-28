'''
Implemente:
Números de 1 a 100 que são múltiplos de 3
Tabuada completa (1 a 10)
Leitura de números até o usuário digitar 0
mostre soma, quantidade e média
Cálculo de fatorial (sem biblioteca)
'''

def multiplos_tres():
    """Retorna uma lista de múltiplos de 3 entre 1 e 100."""
    multiplos = []
    for i in range(1, 101):
        if i % 3 == 0:
            multiplos.append(i)
    return multiplos

def calcular_tabuadas():
    """Imprime as tabuadas do 1 ao 10."""
    for tabuada in range(1, 11):
        print(f"\n--- Tabuada do {tabuada} ---")
        for numero in range(1, 11):
            resultado = numero * tabuada
            print(f"{tabuada} x {numero} = {resultado}")

def processar_entradas():
    """Lê números até digitar 0 e mostra soma, quantidade e média."""
    numeros_entrada = []
    while True:
        try:
            entrada = int(input("Digite um número inteiro (ou 0 para encerrar): "))
            
            if entrada == 0:
                print("Entrada de dados encerrada.")
                break
            
            numeros_entrada.append(entrada)
        except ValueError:
            print("Erro: Digite apenas números inteiros válidos.")
            
    if numeros_entrada:
        soma_total = sum(numeros_entrada)
        qtd = len(numeros_entrada)
        med = soma_total / qtd
        print(f"\nResultados da lista {numeros_entrada}:")
        print(f"Soma: {soma_total}")
        print(f"Quantidade: {qtd}")
        print(f"Média: {med:.2f}")
    else:
        print("Nenhum número foi inserido.")

def fatorial(num):
    """Calcula o fatorial de um número de forma iterativa."""
    if num < 0:
        return "Erro: Não existe fatorial de número negativo."
    if num == 0 or num == 1:
        return 1
    fat = 1
    for i in range(2, num + 1):
        fat *= i
    return fat

# --- EXECUÇÃO DO PROGRAMA ---

print("=== MÚLTIPLOS DE 3 (1-100) ===")
print(multiplos_tres())

# Descomente a linha abaixo para ver a tabuada completa
# calcular_tabuadas()

print("\n=== CÁLCULO DE FATORIAL ===")
n_fatorial = 5
print(f"O fatorial de {n_fatorial} é: {fatorial(n_fatorial)}")

print("\n=== LEITURA DE NÚMEROS ===")
processar_entradas()


    


