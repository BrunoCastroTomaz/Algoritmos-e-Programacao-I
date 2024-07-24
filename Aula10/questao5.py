'''
Faça um programa que receba 3 nºs inteiros e determine o menor dentre eles
O programa deverá ter 2 funções:
entrada() que recebe um número pelo teclado e retorna esse nº lido
menor() que possui como parâmetrosos 3 nºs lidos e retorna o menor entre eles
'''
def entrada():
    numero = int(input())
    return numero
def menor(a,b,c):
    return min(a,b,c)
print("Digite um número: ", end="")
a = entrada()
print("\nDigite outro número: ", end="")
b = entrada()
print("\nDigite o último número: ", end="")
c = entrada()
print("\nO menor número é", menor(a,b,c))
    
