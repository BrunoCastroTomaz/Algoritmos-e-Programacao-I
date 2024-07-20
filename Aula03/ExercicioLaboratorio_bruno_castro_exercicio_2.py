'''
Exercícios para entrega
Autor: Bruno Castro Tomaz
DATA: 31/08/2021
Disciplina: Algoritmos e Programação 01
'''
#Exercício 2
'''
Descrição do algoritmo: O programa deve receber um número de 3 dígitos e
apresentá-lo invertido.
'''

Num = int(input("Digite um numero de 3 dígitos: "))
digito1 = (Num%100)%10
digito2 = (Num%100)//10
digito3 =  Num//100
num_invertido = digito1*100 + digito2*10 + digito3
print("numero invertido= ",num_invertido)
