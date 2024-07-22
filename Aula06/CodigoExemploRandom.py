#exemplo de codigo que gera numeros aleatórios

#importando o módulo random
import random

#exemplos
valor1 = random.randint(65,300)
#a função randint retornará um número inteiro aleatório.
# Nesse caso, no intervalo [65,300]
print("valor1 = ", valor1)

valor2 = random.randrange(80, 121, 2)
#a função randrange retornará um número inteiro aleatório.
#Nesse caso, de 80 a 120 de 2 em 2
print("valor2 = ", valor2)

valor3 = random.random()
#a função random retornará um número real no intervalo [0,1]
print("valor3 = ", valor3)
