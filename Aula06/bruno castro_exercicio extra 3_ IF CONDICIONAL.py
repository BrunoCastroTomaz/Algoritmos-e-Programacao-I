'''''
AUTOR: BRUNO CASTRO TOMAZ
DATA: 01/10/2021
ALGORITMOS E PROGRAMAÇÃO 1

EXERCICIO EXTRA 3
MENU DE OPERAÇÕES
'''''

#treinando funções def e também comando while

def media():
    n1 = int(input("Primeiro número: "))
    n2 = int(input("Segundo número: "))
    print(f"A média entre os números digitados é {(n1+n2)/2}")

def diferenca():
    n1 = int(input("Primeiro número: "))
    n2 = int(input("Segundo número: "))
    print(f"A diferença entre os números digitados é {n1-n2}")

def produto():
    n1 = int(input("Primeiro número: "))
    n2 = int(input("Segundo número: "))
    print(f"O produto entre os números digitados é {n1*n2}")

def divisao():
    n1 = int(input("Primeiro número: "))
    n2 = int(input("Segundo número: "))
    while n2 == 0:
        n2 = int(input("Ops... valor inválido! Insira um número diferente de 0: "))
    print(f"A divisao entre os números digitados é {n1/n2}")

def enter():
    input("Pressione ENTER para continuar....")

def menu():
    print("====MENU====")
    print("1) Média entre os números digitados")
    print("2) Diferença do maior pelo menor")
    print("3) Produto entre os números digitados")
    print("4) Divisão do primeiro pelo segundo")

def main():
    while True:
        menu()
        option = int(input("Insira sua opção: "))
        if option == 1:
            media()
            enter()
        elif option == 2:
            diferenca()
            enter()
        elif option == 3:
            produto()
            enter()
        elif option == 4:
            divisao()
            enter()
        else:
            print("opção inválida!")
            break
main()
