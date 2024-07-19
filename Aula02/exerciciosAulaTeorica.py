'''
Escreva	um  programa, que receba o salário de um funcionário e o percentual de aumento a ser aplicado  sobre o salário. Calcule e apresente
o valor do aumento e o novo salário. Exemplo: para um salário de 2000.00 e um percentual de aumento de 15%, o valor do aumento será 300.00 e o novo salário 2300.00.
'''
salario = float(input("Informe o seu salário: "))
percentualAumento = int(input("Informe o percentual de aumento: "))
aumento = (percentualAumento * salario)/ 100
print(f"Para um salario de {salario} o valor do aumento será de {aumento} e o novo salário {salario+aumento}")


#Elabore um  programa que leia três notas, calcule e mostre a média aritmética entre elas
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
media = (nota1 + nota2 + nota3)/3
print(f"A média aritmética entre as notas é: {media}")


#Elabore um  programa que receba três notas e seus respectivos pesos, calcule e mostre a média ponderada dessas notas.
notaA = float(input("Informe a primeira nota: "))
pesoA = float(input("Informe o peso da primeira nota: "))
notaB = float(input("Informe a segunda nota: "))
pesoB = float(input("Informe o peso da segunda nota: "))
notaC = float(input("Informe a terceira nota: "))
pesoC = float(input("Informe o peso da terceira nota: "))
media = (notaA*pesoA + notaB*pesoB + notaC*pesoC)/(pesoA + pesoB + pesoC)
print(f"A média ponderada entre as notas é: {media}")


'''
Sabe-se	que o valor de cada 1000 litros	de água corresponde a 2% do salário mínimo.  Elabore um	programa que receba o valor do salário mínimo
e a quantidade de água consumida em uma residência por mês. Calcule e mostre:
a) O valor da conta de água.
b) O valor a ser pago com desconto de 15%.
'''
salarioMinimo = float(input("Escreva o salário mínimo: "))
qtdeAgua = float(input("Informe a quantidade de água consumida por mês: "))
contaValor = (qtdeAgua/1000) * ((2*salarioMinimo)/100)
print(f"a) O valor da conta de água: {contaValor}")
print(f"b) O valor a ser pago com desconto: {((85*contaValor)/100)}")


'''
Escreva	um programa em  Python	que o usuário digita dois números inteiros e armazena em duas variáveis  n1 e n2, o seu	programa deve trocar os valores
dessas	variáveis, de maneira que o valor de n1 seja igual ao de n2 e vice-versa, e depois deve exibir os números lidos com valores trocados.
'''
n1 = int(input())
n2 = int(input())
n1, n2 = n2, n1
print(f"Primeiro valor lido (trocado): {n1}")
print(f"Segundo valor lido (trocado): {n2}") 


'''
Escreva	um programa em Python que peça para o usuário digite um texto (mensagem: “Digite  um	texto:	”) e depois para digitar um número
(mensagem: “Digite um número”). Depois,	deve mostrar duas mensagens: 1) “A primeira entrada é  um dado do tipo <tipo>”;	2) “A segunda entrada
é do tipo <tipo>”, em que <tipo> deve ser trocado pelo tipo dos dados de entrada do usuário
'''
texto = input("Digite um texto: ")
numero = input("Digite um número: ")
print(f"A primeira entrada é um dado do tipo {type(texto)}")
if numero.isnumeric():
    print("A segunda entrada é do tipo numérico")
else:
    print(f"A segunda entrada é do tipo {type(numero)}")
