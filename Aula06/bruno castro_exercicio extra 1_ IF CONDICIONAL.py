'''''
AUTOR: BRUNO CASTRO TOMAZ
DATA: 01/10/2021
ALGORITMOS E PROGRAMAÇÃO 1

EXERCICIO EXTRA 1
PROBLEMA DA  TARIFA
'''''

print("N\tNoturno\nD\tDiurno\n")
TIPO=input("insira o tipo de vôo: ")
quantidade = int(input("Insira a quantidade de pessoas: "))
if (TIPO=="D") and (quantidade<=50):
    tarifa = 200.00
elif (TIPO=="D") and (quantidade>50):
    tarifa = 120.00
elif (TIPO=="N") and (quantidade<=50):
    tarifa = 100.00
elif (TIPO=="N") and (quantidade>50):
    tarifa = 80.00

print("Tarifa-> R$",tarifa)

total=quantidade*tarifa

print("total a pagar: ",total)
