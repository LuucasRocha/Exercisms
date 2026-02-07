'''
 Um vendedor necessita de um algoritmo que calcule o preço total devido por um cliente. O algoritmo deve receber o código de um produto e a quantidade comprada e calcular o preço total, usando a tabela abaixo:
 
Código do Produto	Preço unitário
1001	                5,32
1324                	6,45
6548	                2,37
0987	                5,32
7623	                6,45
'''

def converter_tempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    
    return horas, minutos, segundos_restantes

print(converter_tempo(24942085))

