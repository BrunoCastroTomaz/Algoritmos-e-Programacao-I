"""""""""""""""""""""""
Exercícios para entrega
Autor: Bruno Castro Tomaz
DATA: 31/08/2021
Disciplina: Algoritmos e Programação 01
"""""""""""""""""""""""

#Exercício 1
"""""""""
Descrição do algoritmo: Este programa calcula e apresenta a quantidade total de
combustível (litros) gasto em uma viagem, bem como a distância percorrida pelo automóvel.
Para realização do cálculo, o usuário deve inserir as medidas de tempo e velocidade média.
"""""""""
TEMPO=int(input("Por favor, digite o tempo (h) gasto na viagem: "))
VELOCIDADE=int(input("Ótimo!\nAgora forneça a velocidade média (km/h): "))
DISTANCIA=TEMPO*VELOCIDADE
LITROS_USADOS=DISTANCIA/12
print("Nestas condições(velocidade média=",VELOCIDADE,";tempo gasto=",TEMPO,") conclui-se que a distância percorrida pelo automóvel foi de",DISTANCIA,"Km;e que a quantidade de litros gastos na viagem equivale a ",LITROS_USADOS,"L")

