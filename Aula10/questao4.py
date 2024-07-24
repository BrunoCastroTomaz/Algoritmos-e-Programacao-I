'''
Faça um programa que leia um vetor de 5 nºs reais e mostre-os na ordem inversa.
O programa deverá ter 3 funções:
entrada() que recebe os 5 nºs reais
saida() que coloca em ordem inversa e imprime 
main() que chama as duas funções anteriores
'''
def entrada():
    global vetor
    vetor = []
    for i in range(5):
        n = float(input(f"Digite o {i+1}º número: "))
        vetor.append(n)
def saida():
    vetor.reverse()
    print(vetor)
def main():
    entrada()
    saida()
main()
