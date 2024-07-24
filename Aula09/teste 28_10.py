'''
Escreva um programa que possua uma função que retorna o maior de dois números
passados como parâmetro. Adicionalmente possui uma outra função que receber um
número digitado pelo usuário e não possui parâmetro. O programa principal deverá ter a
chamada destas duas funções para ler os números digitados e imprimir o maior dos dois
números.
'''

def entrada ():
    num=float(input())
    return num

def maior (a,b):
    if a>b:
        return a
    else:
        return b
    #ou então isso aqui
    #return max(a,b)
    
def main():
    a= entrada()
    b= entrada()
    print("o maior valor é : ", maior(a,b))
main()
