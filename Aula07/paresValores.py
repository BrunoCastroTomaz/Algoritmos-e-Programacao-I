'''
Faça um programa que leia um número não determinado de pares de valores [m,n], todos inteiros e positivos,
um par de cada vez, e que calcule e mostre a soma de todos os números inteiros entre m e n. A digitação
de pares terminará quando m for maior ou igual a n
'''

#função que converte a string lida como input do usuário, em par de valores inteiros
def converteStringEntrada():
    valores = input("Informe um par de valores conforme exemplo - m,n - : ")
    valores = valores.split(',')
    m  = int(valores[0])
    n  = int(valores[1])
    return m,n
def main():
    while True:
        m,n = converteStringEntrada()            
        while m <= 0 or n <=0:
            print("por favor informe valores inteiros e positivos!")
            m,n = converteStringEntrada()
        if m >= n:
            break
        else:
            soma = 0 
            print("Números inteiros no intervalo: ")
            for i in range(m, n+1):
                print(i,end=" ")
                soma+=i
            print("\nA soma de todos os números é:", soma)
main()
