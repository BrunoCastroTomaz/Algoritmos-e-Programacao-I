import time

#Escreva um programa para escrever os 10 primeiros múltiplos de 3:
i  = 1
while i <= 10:
    print(f"{3*i} ", end="")
    i += 1
print("\n")

#imprimir tabuadas de multiplicação de 1 a 10
tabuada =1
while tabuada <= 10:
    numero =1
    while numero <= 10:
        print(f"{tabuada} X {numero} = {tabuada*numero}", end="\t")
        numero +=1
    print("\n")
    tabuada += 1

#Escreva um programa para escrever na tela a contagem regressiva do lançamento de um foguete. O programa deve
#exibir 10, 9, 8, ...., 1, 0 e Fogo! Utilize um temporizador de 1 segundo

#treinando método sleep da biblioteca time
x = 10
while x >= 0:
    if x == 0:
        print("e Fogo!")
    else:
        print(x, end=" ")
    time.sleep(1)
    x -= 1

'''
Escreva um programa que leia duas notas de n alunos. Calcule e apresente:
- a média de cada aluno (aritmética);
- a quantidade de alunos aprovados (média superior ou igual a 6.0);
- a quantidade de alunos reprovados (média inferior a 6.0).
Validar:
- quantidade de alunos: só aceitar de 1 a 200;
- nota: só aceitar de 0.0 a 10.0.
'''

n = int(input("Informe a qtde de alunos: "))
while n < 1 or n > 200:
    n = int(input("Por favor, informe uma qtde entre 1 e 200: "))
print('\n')
medias = []
media = 0
aprovados = 0
reprovados = 0
for i in range(n):
    notaA = float(input(f"Aluno {i} nota A: "))
    while notaA < 0.0 or notaA > 10.0:
        notaA = float(input("Por favor, informe uma nota entre 0 e 10: "))
    notaB = float(input(f"Aluno {i} nota B: "))
    while notaB < 0.0 or notaB > 10.0:
        notaB = float(input("Por favor, informe uma nota entre 0 e 10: "))
    print('\n')
    media = (notaA+notaB) / 2
    if media >= 6.0:
        aprovados +=1
    else:
        reprovados +=1
    medias.append(media)
print("Qtde de alunos aprovados:", aprovados)
print("Qtde de alunos reprovados:", reprovados)
print("Média por aluno:")
for i in range(n):
    print(f"Aluno {i}\t{medias[i]}")


'''
Escreva um programa que lê dois números e calcula a multiplicação entre os
números dados. Porém, sem o uso do operador *, mas pela soma sucessiva de um
deles. Exemplo: 3 x 4 = 3 + 3 + 3 + 3 = 4 + 4 + 4 = 12
'''

num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))
i = 1
while i < num2:
    num1 += num1/i
    i+=1
print("O resultado da multiplicação é", num1)


'''
Crie um algoritmo que leia um número e desenhe o seguinte padrão na tela. Exemplo:
número = 4
****
****
****
****
'''
numero = int(input("Fala um número: "))
if numero == 0:
    print()
elif numero == 1:
    print("*")
else:
    i = 0
    while i < numero:
        j = 0
        while j < numero:
            print("*",end="")
            j+=1
        print()
        i+=1
