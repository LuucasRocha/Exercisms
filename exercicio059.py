#Buscar número em agenda de contatos
def main():
    print(buscar_numero("Maria"))

nomes = [
    {"Nome": "Carter", "Number": "2798835903"},
    {"Nome": "Alex", "Number": "2798835904"},
    {"Nome": "Maria", "Number": "2798835905"},
]

def buscar_numero(nome):
    for contato in nomes:
        if contato["Nome"] == nome:
            return contato["Number"]
    return "Não encontrado"

main()