#teste
for i in range(10):
    print(i)
    i = 5             # this will not affect the for-loop
                      # because i will be overwritten with the next
                      # index in the range
#exercitando dicionários
gatinhos = {"Português": "gato", "Inglês": "cat", "Francês": "chat", "Finlandês": "Kissa"}
for chave, valor in gatinhos.items():
    print(chave, "->", valor)


"""
Esse código deve rodar até que a palavra "sair" seja digitada.
* Caso uma palavra com 2 ou menos caracteres seja digitada, um aviso
  deve ser exibido e o loop será executado do início (devido ao
  continue), pedindo uma nova palavra ao usuário.
* Caso qualquer outra palavra diferente de "sair" seja digitada, um
  aviso deve ser exibido.
* Por fim, caso a palavra seja "sair", uma mensagem deve ser exibida e o
  loop deve ser encerrado (break).
"""
while True:
    string_input = input("Digite uma palavra: ")
    if string_input.lower() == "sair":
        print("Fim!")
        break
    elif len(string_input) < 2:
        print("String muito pequena... tente novamente")
        continue
    print("Tente digitar \"sair\" ")

'''
Faça um programa que leia um número n (positivo) que indique quantos valores inteiros e
positivos devem ser lidos a seguir. Para cada número lido, mostre uma tabela contendo o valor
lido e o fatorial desse valor.
'''
n = int(input("Fale um número: "))
while n <= 0:
    n = int(input("Por favor, digite um número inteiro positivo: "))
if n > 1:
    print(f"Devem ser lidos {n} números")
    for i in range(n):
        numero = int(input("Fale o número: "))
        if numero == 0:
            print(f"Número lido: {numero}\tFatorial: 1")
            continue
        fatorial = numero
        for i in range(numero-1,1, -1):
            fatorial = fatorial*i
        print(f"Número lido: {numero}\tFatorial: {fatorial}")
else:
    print(f"Deve ser lido {n} número")
    numero = int(input("Fale o número: "))
    if numero == 0:
        print(f"Número lido: {numero}\tFatorial: 1")
    else:
        fatorial = numero
        for i in range(numero-1,1, -1):
            fatorial = fatorial*i
        print(f"Número lido: {numero}\tFatorial: {fatorial}")


#Escreva um programa que receba 50 números inteiros, calcule e mostre a soma dos pares positivos.
soma = 0
for i in range(10):
    n = int(input(f"Número {i+1} : "))
    if n > 0 and n%2 == 0:
        soma+=n
print("Soma total dos pares positivos:", soma)


#Escreva um programa para exibir todos os números pares de 0 até o número informado pelo usuário, sem a utilização do if para avaliar se o número é par
numero = int(input("Informe um nº: "))
for i in range(0, numero+1, 2):
    print(i)
