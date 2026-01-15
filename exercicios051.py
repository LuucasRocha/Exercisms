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

alunos = list()

try:
    quant_aluno = int(input("Quantos alunos deseja cadastrar: "))
except ValueError:
    print("Entrada inválida, digite um número.", end=' ')
    
for i in range(quant_aluno):
    aluno = dict()
    nome = input("Digite o nome do aluno: ")
    media = float(input("Digite a média do aluno: "))
    
    aluno['nome'] = nome
    aluno['media'] = media
    
    if media > 7:
        aluno['Situação'] = "Aprovado"
    else:
        aluno['Situação'] = "Reprovado"
        
    alunos.append(aluno)
    
for i, aluno in enumerate(alunos, start=1):
    print(f"\nDados do aluno {i}: ")
    for k, v in aluno.items():
        print(f"{k}: {v}")
    
    