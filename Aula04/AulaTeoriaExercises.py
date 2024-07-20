'''
Exercicios teoricos
Autor: Bruno Castro Tomaz
DATA ATUAL: 02/09/2021
'''

# Resolução de expressões lógicas
print((not (1 ==2)) and (3<4))
print((1 < 2) or (3>4))
print(((2==2) and (3>4)) or (3 > 4))

# Escreva um programa que leia dois numeros distintos e apresente o quadrado do maior numero
numero1 = int(input())
numero2 = int(input())
if numero1 > numero2:
    print("Quadrado do maior número:", numero1**2)
else:
    print("Quadrado do maior número:", numero2**2)

# Escreva um programa que leia um numero inteiro e exiba se ele é um numero par ou impar
numeroInt = int(input())
if numeroInt %2 == 0:
    print("Este número é par!")
else:
    print("Este número é impar!")


'''
Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da
compra for menor que R$ 20,00; caso contrário, o lucro será de 30%. Escreva um programa que
receba o valor do produto e exiba o valor da venda.
'''

valorProduto = float(input("Informe o valor do produto: "))
if valorProduto < 20.0:
    valorVenda = valorProduto*0.45 + valorProduto
else:
    valorVenda = valorProduto*0.30 + valorProduto
print("Valor da venda: ", valorVenda)


'''
As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem
compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule
e escreva o custo total da compra.
'''
macas = int(input("Qtde de maçãs compradas: "))
if macas >= 12:
    print("Custo total da compra: R$ %.2f" %macas)
else:
    print("Custo total da compra: R$ %.2f" %(macas*1.30))
