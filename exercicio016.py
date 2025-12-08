'''
Peça ao usuário uma senha e valide se ela atende aos critérios:
Mínimo de 8 caracteres
Pelo menos uma letra maiúscula
Pelo menos um número
Pelo menos um caractere especial (!@#$%&*)
'''

def validar_senha(senha):
    return (
        len(senha) >= 8 and
        any(c.isupper() for c in senha) and
        any(c.isdigit() for c in senha) and
        any(c in "!@#$%&*" for c in senha)
    )

validar_senha()


