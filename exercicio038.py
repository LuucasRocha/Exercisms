#Crie a função remover_duplicados()

def remover_duplicados(lista):
    nova_lista = []
    
    for num in lista:
        if num not in nova_lista:
            nova_lista.append(num)
    
    return nova_lista

lista_entrada = []

try:
    for i in range(1, 6):
        entrada = int(input(f"Digite o {i}º número: "))
        lista_entrada.append(entrada)

except ValueError:
    print("Erro. Digite apenas números inteiros.")
 
   
sem_duplicados = remover_duplicados(lista_entrada)

print(f"Lista completa: {lista_entrada}")
print(f"Lista sem duplicados: {sem_duplicados}")
    