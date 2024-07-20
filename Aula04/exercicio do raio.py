import math
raio=int(input("Por favor, forneça o raio da esfera: "))
volume= (4*math.pi*pow(raio,3))/3
##########exercicios de aula
#1
print("O volume desta esfera equivale a",volume,"\nEspero ter ajudado")
b=int(input("b="))
a=int(input("a="))
c=int(input("c="))
delta=math.sqrt((math.pow(b,2)-4*a*c))
x1=(-b+delta)/2*a
x2=(-b-delta)/2*a
print("x1=",x1,";x2=",x2)



