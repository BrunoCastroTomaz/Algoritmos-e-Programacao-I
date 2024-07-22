'''
Faça um programa que leia três números inteiros e encontra o menor deles.
Sugestão: Sejam 3 números A, B e C. A ideia principal é: verificar se A é menor que B e C e se não for,
verificar entre B e C
'''
A = int(input())
B = int(input())
C = int(input())
if A <= B and A <= C:
    print("O menor é", A)
elif B <= C:
    print("O menor é", B)
elif C <= B:
    print("O menor é", C)


'''
Faça um programa que leia três números inteiros e colocá-los em ordem crescente.
Sugestão: Sejam 3 números A, B e C. A ideia principal é:
– armazenar em A o menor valor
– armazenar em B o valor intermediário
– armazenar em C o maior valor
'''
A = int(input()) 
B = int(input()) 
C = int(input()) 
if A > B:
    A,B = B,A
if A > C:
    A,C = C,A
if B > C:
    B,C = C,B
print(A,B,C)

