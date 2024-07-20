import math

'''
Faça um Programa que peça a
temperatura em graus Fahrenheit,
transforme e	mostre a temperatura em
graus	Celsius,	sabendo	que:		
c   = 5*(f-32)/9
'''

farenheit = float(input("Forneça a temperatura em Farenheit: "))

celsius = 5 * (farenheit-32)/9

print(f"Temperatura em graus Farenheit: {farenheit} ºF\nTemperatua em graus Celsius: {celsius} ºC")


#Imprime valor absoluto
print(math.fabs(20))

#Escreva um programa que receba o raio de uma esfera, calcule e apresente o seu volume.
raioEsfera = float(input("Informe o raio da esfera: "))
volume = (4*math.pi*math.pow(raioEsfera,3))/3
print("Volume da esfera:", volume)


#Leia um número inteiro de 3 dígitos, determine e apresente o número invertido (exemplo: número informado = 345, número apresentado = 543).
numero = int(input("Digite um número inteiro de 3 dígitos: "))
numeroInvertido = 100*(numero%10) + 10*((numero//10)%10) + numero//100
print("Numero invertido:",numeroInvertido)

#Leia as coordenadas (x,y) de dois pontos no plano cartesiano, calcule e mostre a distância entre os dois pontos.
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
distancia = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))
#experimentando função round()
print("Distancia entre os dois pontos é " , distancia) 
print("Distancia entre os dois pontos é " , round(distancia)) #arredonda para o inteiro mais próximo
print("Distancia entre os dois pontos é " , round(distancia,2)) #arredonda para duas casas decimais

#Desenvolva um programa para converter a temperatura de Celsius para Fahrenheit. A fórmula de conversão	é:  f = (c * 9/5) + 32
celsius = float(input("Informe a temperatura em Celsius: "))
farenheit = (celsius*9/5) + 32
#praticando replace
print("Temperatura em Farenheit: farenheit".replace("farenheit", str(farenheit)))


'''
Escreva	um  programa que permite ao usuário digitar dois números inteiros e exibir  o resultado	para cada uma das seguintes operações:
+,	-,	*,	/,	//,	%,	**
'''

numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite outro inteiro: "))
print(f"{numero1} + {numero2} = {numero1+numero2}")
print(f"{numero1} - {numero2} = {numero1-numero2}")
print(f"{numero1} * {numero2} = {numero1*numero2}")
print(f"{numero1} / {numero2} = {numero1/numero2}")
print(f"{numero1} // {numero2} = {numero1//numero2}")
print(f"{numero1} % {numero2} = {numero1%numero2}")
print(f"{numero1} ** {numero2} = {numero1**numero2}")


'''
Três	amigos,	Carlos,	André	e	Felipe,	decidiram	rachar	igualmente	a	conta	em	um	bar.	Faça	um
programa	para	ler o	valor	total	da	conta	e	imprimir	quanto	cada	um	deve	pagar,	mas	faça	com	
que	 Carlos	e	André	 não	 paguem	 centavos.	 Por	exemplo:	 uma	 conta	 de	 R$101,53	 resulta	em
R$33,00	para	Carlos,	R$33,00	para	André	e	R$	35,53	para	Felipe.
'''

totalConta = float(input("Informe o valor total da conta: "))
Carlos = totalConta//3
Felipe = totalConta - Carlos - Carlos
print(f"Carlos pagará {Carlos} ; André pagará {Carlos}; Felipe pagará {Felipe}")
