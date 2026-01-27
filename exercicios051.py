'''
Cadastro Simples de Alunos 
Objetivo: Criar um programa que cadastre o nome e a média de um aluno e armazene essas informações em um dicionário, incluindo a situação (Aprovado/Reprovado). 
Instruções:
Crie um dicionário vazio.
Peça ao usuário para inserir o nome e a média do aluno.
Armazene o nome como uma chave 'nome' e a média como uma chave 'media'.
Adicione uma chave 'situacao' com o valor 'Aprovado' se a média for maior ou igual a 7.0, e 'Reprovado' caso contrário.
No final, exiba o conteúdo do dicionário de forma organizada. 
'''

while True:
    try:
        quantidade_alunos = int(input("Digite a quantidade de alunos que deseja cadastrar: "))
        if quantidade_alunos < 0:
            print("Por favor, digite um número inteiro.")
            continue
        break
    except ValueError:
        print("Entrada inválida.", end=' ')
    
lista_alunos = list()

for i in range(quantidade_alunos):
    aluno = dict()
    
    nome = input(f"Digite o nome do {i + 1}º aluno: ")
    media = float(input(f"Digite a média de {nome}: "))
    
    aluno['Nome'] = nome
    aluno['Media'] = media
    
    if media <= 7:
        aluno['Situação'] = "Reprovado"
    else:
        aluno['Situação'] = "Aprovado"
    
    lista_alunos.append(aluno)

print("=-" * 5, "Lista dos alunos",  "-=" * 5)
for i, aluno in enumerate(lista_alunos, start = 1):
    print(f"\nSituação do aluno {i}: ")
    for k, v in aluno.items():
        print(f"{k}: {v}")