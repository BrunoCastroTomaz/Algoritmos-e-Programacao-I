'''''
AUTOR: BRUNO CASTRO TOMAZ
DATA: 25/10/2021
ALGORITMOS E PROGRAMAÇÃO 1

EXERCICIOS para ENTREGA: Exercicio 5

Elabore um programa que calcule e apresente a soma dos inteiros existentes entre dois valores
lidos. Considere que o segundo número lido deve ser maior que o primeiro número lido
'''''
num1=int(input("Insira um número inteiro: "))
num2= int(input("insira outro: "))
while num2<=num1:
    print ("valor inválido: Num2 deve ser maior que num1")
    num2= int(input("num2: "))
soma=0
for i in range (num1+1,num2,1):
    soma= soma+i
print("A soma dos inteiros existentes entre estes valores é de: ", soma)
