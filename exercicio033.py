# Crie um fluxo para decidir se uma pessoa pode votar (idade >= 16).

def autentica_vot(idade):
    if not isinstance(idade, int):
        return "Idade inválida"
    return True if idade >= 16 else False

entrada = ""

status_vot = autentica_vot(entrada)
print(status_vot)