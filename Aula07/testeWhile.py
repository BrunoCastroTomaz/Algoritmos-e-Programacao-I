numero =  1
while numero <= 10:
    print(numero)
    numero+=1
print("FIM")

while numero != 0:
    numero = int(input("Digite um número: "))
print("FIM")

#teste booleano - true
soma = 0
while True:
    vlr = int(input("Digite um número: "))
    if vlr == 0:
        break
    soma += vlr
print("Soma: ", soma)

#imprimindo númmeros de 50 a 100
x = 50
while x <=100:
    print(x)
    #print(x,end="") #mesma linha, sem espaços em branco
    #print("%d "%x,end="") #mesma linha, COM espaços em branco
    #print("%d, "%x,end="") #mesma linha, COM espaços em branco e COM VIRGULA
    x += 1
