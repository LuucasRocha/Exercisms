'''
Cadastro Simples de Alunos (Iniciante)
Objetivo: Criar um programa que cadastre o nome e a média de um aluno e armazene essas informações em um dicionário, incluindo a situação (Aprovado/Reprovado). 
Instruções:
Crie um dicionário vazio.
Peça ao usuário para inserir o nome e a média do aluno.
Armazene o nome como uma chave 'nome' e a média como uma chave 'media'.
Adicione uma chave 'situacao' com o valor 'Aprovado' se a média for maior ou igual a 7.0, e 'Reprovado' caso contrário.
No final, exiba o conteúdo do dicionário de forma organizada. 
'''

# Criar uma lista vazia para armazenar os dicionários dos alunos
alunos = []

# Perguntar quantos alunos deseja cadastrar
num_alunos = int(input("Quantos alunos você deseja cadastrar? "))

# Loop para cadastrar cada aluno
for i in range(num_alunos):
    print(f"\nCadastrando aluno {i+1}:")
    
    # Criar um dicionário vazio para o aluno atual
    aluno = {}
    
    # Pedir ao usuário para inserir o nome do aluno
    nome = input("Digite o nome do aluno: ")
    
    # Pedir ao usuário para inserir a média do aluno
    media = float(input("Digite a média do aluno: "))
    
    # Armazenar o nome e a média no dicionário
    aluno['nome'] = nome
    aluno['media'] = media
    
    # Adicionar a chave 'situacao' com base na média
    if media >= 7.0:
        aluno['situacao'] = 'Aprovado'
    else:
        aluno['situacao'] = 'Reprovado'
    
    # Adicionar o dicionário do aluno à lista
    alunos.append(aluno)

# Exibir o conteúdo de todos os alunos de forma organizada
print("\nDados de todos os alunos:")
for i, aluno in enumerate(alunos, start=1):
    print(f"\nAluno {i}:")
    for chave, valor in aluno.items():
        print(f"  {chave.capitalize()}: {valor}")
