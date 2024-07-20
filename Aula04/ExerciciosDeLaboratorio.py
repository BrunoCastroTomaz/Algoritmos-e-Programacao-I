# Faça um programa que leia um número e mostre uma mensagem indicando se este número é positivo ou negativo.
numero = input("Fala um numero aí: ")
if numero.isdigit(): #Returns True if all characters in the string are digits
    print("Esse número é positivo")
else:
    print("Esse número é negativo")

#Faça um programa que apresenta o maior de dois números lidos do usuário.
A = int(input("Fala outro numero: "))
B = int(input("Fala mais um numero: "))
if A > B:
    print(f"{A} é o maior número")
else:
    print(f"{B} é o maior número")

#Faça um programa que coloque dois nomes em ordem alfabética
nome1 = input("informe seu nome: ").upper() #coloca string em maiúsculo
nome2 = input("Informe o nome do seu amigo: ").upper()

if nome1 < nome2:
    print(f"{nome1}\n{nome2}")
else:
    print(f"{nome2}\n{nome1}")


'''
Elabore um programa que leia do teclado o sexo de uma pessoa. Se o sexo digitado for “M” ou
“m” ou “F” ou “f”, escrever na tela “Sexo válido!”. Caso contrário, exibir “Sexo inválido!”
'''
sexo = input("Digite o sexo 'm' ou 'f': ").lower()
if sexo == 'm' or sexo == 'f':
    print("Sexo válido!")
else:
    print("Sexo inválido!")

'''
Num determinado Estado, para transferências de veículos, o DETRAN cobra uma taxa de 2,5%
para carros fabricados antes de 2010 e uma taxa de 3,5% para os fabricados de 2010 em diante,
taxa esta incidindo sobre o valor de tabela do carro. Escreva um programa lê o ano e o preço do
carro e a seguir calcula e imprime a taxa a ser paga.
'''
ano= int(input("ANO do carro: "))
preco=float(input("Preço do carro: "))
if(ano<2010):
    taxa=preco*0.025
else:
    taxa=preco*0.035
print(f"O ano do carro: ",ano,"\nPreço carro: R${preco},\nTaxa a ser paga: ",taxa)


#Escreva um programa que leia um número inteiro de 3 dígitos e imprima se o algarismo da dezena é par ou ímpar.
num3digitos = int(input("Escreva um numero inteiro de 3 digitos: "))
num3digitos = num3digitos%100
num3digitos = num3digitos//10
if num3digitos % 2 == 0:
    print("O algarismo da dezena é par!")
else:
    print("O algarismo da dezena é impar!")

'''
Um pescador comprou um computador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca
do Estado de São Paulo (50 quilos), deve pagar uma multa de R$ 4,00 por quilo excedente.
Escreva um programa que leia o peso de peixes, e verifique se há excesso. Se houver, determine
o peso excedente e o valor da multa. Caso contrário, mostrar “Dentro do regulamento”
'''
peso = float(input("Peso de peixes: "))
if peso <= 50.0:
    print("Dentro do regulamento")
else:
    excedente = peso - 50.0
    multa = excedente *  4.00
    print(f"Peso excedente: {excedente}\nValor da multa: R$ {multa}")
