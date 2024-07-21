'''
Escreva um programa para ler as coordenadas (X,Y) de um ponto no sistema cartesiano e escrever o quadrante ao qual o ponto pertence.
Caso o ponto não pertença a nenhum quadrante, escrever se ele está sobre o eixo X, eixo Y ou na origem. Considere que o usuário poderá
informar qualquer valor para as coordenadas.
'''
#ENTRADAS
x = float(input("x = "))
y = float(input("y = "))

#PROCESSAMENTO
if x == 0 and y == 0:
    print("O ponto está sobre a origem")
elif x == 0 and y != 0:
    print("O ponto está sobre o eixo Y")
elif y == 0 and x != 0:
    print("O ponto está sobre o eixo X")
elif x > 0 and y > 0:
    print("O ponto pertence ao primeiro Quadrante (I)")
elif x > 0 and y < 0:
    print("O ponto pertence ao Quarto Quadrante (IV)")
elif x < 0 and y > 0:
    print("O ponto pertence ao Segundo Quadrante (II)")
elif x < 0 and y < 0:
    print("O ponto pertence ao Terceiro Quadrante (III)")

    
