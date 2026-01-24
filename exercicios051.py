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

alunos = list()

for i in range(3):
    aluno = dict()
    nome = input("Digite o nome do aluno: ")
    media = float(input("Digite a média do aluno: "))
    
    aluno['Nome'] = nome
    aluno['Media'] = media
    
    if media >= 7:
        aluno['Situação'] = "Aprovado"
    else:
        aluno['Situação'] = "Reprovado"
    
    alunos.append(aluno)
    
print(alunos)
    
    
    