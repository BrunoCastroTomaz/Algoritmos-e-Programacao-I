'''''
AUTOR: BRUNO CASTRO TOMAZ
DATA: 25/10/2021
ALGORITMOS E PROGRAMAÇÃO 1

EXERCICIOS para ENTREGA: Exercicio 3

Faça um programa que receba a idade, a altura e o peso de 30 pessoas, calcule e mostre:
a) a quantidade de pessoas com idade superior a 50 anos;
b) a média das alturas das pessoas com idade entre 10 e 20 anos;
c) a porcentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas.
'''''
conta_idade=0
conta_alturas=0
conta_peso=0
soma_alturas=0.0
for i in range(30):
    print("pessoa", i+1)
    idade = int(input("Forneça sua idade: "))
    altura = float(input("Forneça sua altura: "))
    peso = float(input("Insira seu peso: "))
    print("\n")
    if (idade>50):
        conta_idade+=1
    if ((idade>=10) and (idade<=20)):
        conta_alturas+=1
        soma_alturas = soma_alturas + altura
    if (peso<40.0):
        conta_peso+=1
#letra a
print("A quantidade de pessoas com idade superior a 50 anos é de ", conta_idade)
#letra b
if (conta_alturas!=0):
    media = soma_alturas/conta_alturas
print("A média das alturas das pessoas com idade entre 10 e 20 anos equivale a", media)  
#letra c
porcentagem = 100*conta_peso/30
print("A porcentagem de pessoas com peso inferior a 40 kg é de ", porcentagem, "%")
