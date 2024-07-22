'''''
AUTOR: BRUNO CASTRO TOMAZ
DATA: 01/10/2021
ALGORITMOS E PROGRAMAÇÃO 1

EXERCICIO EXTRA 2
PROBLEMA DO IMC
'''''

peso=float(input("fornecer o seu peso(Kg): "))
altura=float(input("Fornecer sua altura(m): "))
IMC = peso/(altura**2)
print("Seu IMC vale ",IMC)
if IMC<20:
    print("Abaixo do peso")
elif (IMC>=20) and (IMC<=25):
    print("Normal")
elif (IMC>25) and (IMC<=30):
    print("Excesso de Peso")
elif (IMC>30) and (IMC<=35):
    print("Obesidade")
elif IMC>35:
    print("Obesidade mórbida")
