"""Receba as notas de um aluno (quantidade indefinida, até o usuário digitar -1).
Depois, mostre:
Média das notas
Maior nota
Menor nota"""

notas = []
while True:
    nota = float(input("Digite uma nota (-1 para sair): "))
    if nota == -1:
        break
    notas.append(nota)
    
media_notas = sum(notas) / len(notas)
maior_nota = max(notas)
menor_nota = min(notas)
    
print(f"Média das nota: {media_notas}")
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")
     