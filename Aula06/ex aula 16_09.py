'''
Faça um programa que faz a leitura de três valores reais (A, B e C), representando os coeficientes
de uma equação do 2o. grau, calcula o valor do delta e os valores das raízes reais, caso existam.
Considere que:
– se A for igual a zero, exiba a mensagem “Não é equação de 2º grau!” e encerre;
– se o delta for negativo, exiba a mensagem “Não existem raízes reais” e encerre.
– Se o delta for zero ou positivo, exibe a raiz ou as raízes e encerre
'''
import math
A=float(input("Insira o coeficiente a da equação: ")
if A==0:
    print("Não é equação do segundo grau!")
else:
    B=float(input("Insira o coeficiente b: ")
    C=float(input("Insira o coeficiente c: ")
    delta=B*B-4*A*C
    if delta<0:
        print("Não existem raízes reais!")
    else:
        x1=(-B + math.sqrt(delta))/2*A
        x2=(-B - math.sqrt(delta))/2*A
        print("Delta=",delta)
        if x1==x2:
            print("raíz=",x1)
        else:
            print("Raízes:\n",x1"\n",x2)
                                
                        
