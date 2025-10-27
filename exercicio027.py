'''
Peça três notas de um aluno, calcule a média, e mostre a situação:
Média < 5 → Reprovado
Média >= 5 e < 7 → Recuperação
Média >= 7 → Aprovado
'''

def aluno_situacao(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    if media >= 7:
        return f"Média: {media:.1f} | Aprovado."
    elif  5 <= media < 7  :
        return f"Média: {media:.1f} | Recuperação."
    else:
        return f"Média: {media:.1f} | Reprovado."
    
nota_aluno_1 = float(input("Digite a nota da n1: "))

nota_aluno_2 = float(input("Digite a nota da n2: "))

nota_aluno_3 = float(input("Digite a nota da n3: "))

situacao = aluno_situacao(nota_aluno_1, nota_aluno_2, nota_aluno_3)
print(f"\n Resultado final: {situacao}")