'''
Faça um programa de calculadora simples com as seguintes operações possíveis: adição,
subtração, multiplicação e divisão. O programa inicia apresentando ao usuário um menu de
opçõess:
********************************************************************* *
Calculadora. Opções possíveis:
* 1. Adição
* 2. Subtração
* 3. Multiplicação
* 4. Divisão
* 5. Sair do programa
*********************************************************************
Entre com sua opcao:
Crie uma função que apresenta o menu inicial acima e retorna a opção do usuário para o
programa principal. Esta opção é então analisada e o programa principal chama as funções
de adição, subtração, multiplicação e divisão conforme a opção do usuário. Se a opção for
inválida, informe ao usuário e peça a ele para entrar com uma opção válida. Após a
execução da operação o programa volta a apresentar o menu inicial até que o usuário
encerre o programa com a opção 5.
'''
def enter():
    print("PRESSIONE ENTER PARA CONTINUAR.....")
    input()
def adicao():
    n1 = int(input("Fala um nº: "))
    n2 = int(input("Fala outro nº: "))
    print("A soma dos números é", n1+n2)
def subtracao():
    n1 = int(input("Fala um nº: "))
    n2 = int(input("Fala outro nº: "))
    print("A subtracao dos números é", n1-n2)
def multiplicacao():
    n1 = int(input("Fala um nº: "))
    n2 = int(input("Fala outro nº: "))
    print("A multiplicacao dos números é", n1*n2)
def divisao():
    n1 = int(input("Fala um nº: "))
    n2 = int(input("Fala outro nº: "))
    print("A divisao dos números é", n1/n2)
def menu():
    print("**********************************************************************")
    print("Calculadora. Opções possíveis:")
    print("* 1. Adição")
    print("* 2. Subtração")
    print("* 3. Multiplicação")
    print("* 4. Divisão")
    print("* 5. Sair do programa")
    print("*********************************************************************")
    
def main():
    menu()
    option = int(input("Entre com sua opção: "))
    while option != 5:
        if option == 1:
            adicao()
            enter()
        elif option == 2:
            subtracao()
            enter()
        elif option == 3:
            multiplicacao()
            enter()
        elif option == 4:
            divisao()
            enter()
        else:
            option = int(input("Opção inválida! Tente novamente: "))
        menu()
        option = int(input("Entre com sua opção: "))
    print("FIM!")
main()
