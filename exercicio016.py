'''
Peça ao usuário uma senha e valide se ela atende aos critérios:
Mínimo de 8 caracteres
Pelo menos uma letra maiúscula
Pelo menos um número
Pelo menos um caractere especial (!@#$%&*)
'''

senha = input("Digite uma senha: ")

def validar_senha(senha):
    if len(senha) < 8:
        return "Senha deve ter no mínimo 8 caracteres."
    if not any(c.isupper() for c in senha):
        return "Senha deve conter pelo menos uma letra maiúscula."
    if not any(c.isdigit() for c in senha):
        return "Senha deve conter pelo menos um número."
    if not any(c in '!@#$%&*' for c in senha):
        return "Senha deve conter pelo menos um caractere especial (!@#$%&*)."
    return "Senha válida!"

resultado = validar_senha(senha)
print(resultado)





