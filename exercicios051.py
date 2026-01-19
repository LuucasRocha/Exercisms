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

lista_alunos = list()

cont_alunos = int(input("Quantos alunos deseja cadastrar: "))

for i in range(cont_alunos):
    aluno = dict()
    
    nome = input(f"Digite o nome do {i + 1}º aluno: ")
    media = float(input(f"Digite a média do {i + 1}º aluno: "))

    aluno['nome'] = nome
    aluno['media'] = media
    if media >= 7:
        aluno['situação'] = "Aprovado"    
    else:
        aluno['situação'] = "Reprovado"
    
    lista_alunos.append(aluno)
    
for i, aluno in enumerate(lista_alunos, start=1):
    print(f"\nDados do aluno {i}: ")
    for k, v in aluno.items():
        print(f"{k}: {v}")