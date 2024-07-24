# BRUNO CASTRO TOMAZ
# EXERCÍCIO DIA 09/11/2021
# LISTAS
# ALGORITMOS E PROGRAMAÇÃO 1 [TURMA: 01N11]

#DECLARAÇÃO DAS LISTAS
jogo1 = ['Brasil','Italia',[10,9]]
jogo2 = ['Brasil','Espanha',[5,7]]
jogo3 = ['Italia', 'Espanha', [7,8]]

#CONTANDO AS FALTAS DE CADA JOGO E TIME 

#JOGO 1
faltas = jogo1[2]
faltas_jogo1 = faltas[0] + faltas[1]
Brasil = faltas[0]
Italia = faltas[1]

#JOGO 2
faltas = jogo2[2]
faltas_jogo2 = faltas[0] + faltas[1]
Brasil = Brasil + faltas[0]
Espanha = faltas[1]

#JOGO 3
faltas = jogo3[2]
faltas_jogo3 = faltas[0] + faltas[1]
Italia = Italia + faltas[0]
Espanha = Espanha + faltas[1]

#RESPOSTA letra A
total_faltas = faltas_jogo1 + faltas_jogo2 + faltas_jogo3
print("A) O total de faltas do campeonato é de ",total_faltas, "faltas")

print("Brasil: ", Brasil)
print("Italia: ", Italia)
print("Espanha: ", Espanha)
      
#RESPOSTA letra B
print ("B) ")
if Brasil == Italia and Brasil == Espanha:
    print("Todos cometeram o mesmo número de faltas")
else:
    faltas = [Brasil, Italia, Espanha]
    faltas.sort()
    if faltas[2] == Brasil:
        print ("Brasil fez mais faltas")
    elif faltas[2] == Espanha:
        print ("Espanha fez mais faltas")    
    else:
        print ("Italia fez mais faltas")    

#RESPOSTA letra C
print ("C) ")
if Brasil == Italia and Brasil == Espanha:
    print("Todos cometeram o mesmo número de faltas")
else:
    faltas = [Brasil, Italia, Espanha]
    faltas.sort()
    if faltas[0] == Brasil:
        print ("Brasil fez menos faltas")
    elif faltas[0] == Espanha:
        print ("Espanha fez menos faltas")    
    else:
        print ("Italia fez menos faltas")
