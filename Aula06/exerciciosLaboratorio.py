#ATIVIDADES DE LABORATÓRIO - DESAFIOS E/OU JOGOS
'''
As atividades de jogos aqui propostas envolvem a geração de um número aleatório.

1) Esse é o jogo dos dados, muito usado em Las Vegas nos cassinos, aposte em um
número que seja o resultado da soma deles e ganhe o seu dinheiro. Crie duas variáveis
para representar os dados e uma para sua aposta, crie uma para armazenar o resultado
e faça a verificação.

2) O Jogo do par ou ímpar é usado onde duas pessoas jogam
geralmente para decidir um impasse, cada um escolhe entre par ou ímpar e
mostra o seu número, a soma entre eles resulta em um número par ou ímpar
e assim é decidido o vencedor. Aqui faremos com a máquina, ela escolherá
um número randômico entre 0 e 10 e você escolherá o seu. Vamos ver quem
é o vencedor!!!

3) Um dos jogos sugeridos para crianças acima de 6 anos é o PEDRA, PAPEL E
TESOURA
Como jogar:
Dois participantes ficam um de frente para o outro e, ao mesmo tempo, jogam uma
das mãos para frente representando um dos três símbolos: pedra (mão fechada),
papel (mão aberta) ou tesoura (dedos indicador e médio estendidos).
Para definir o vencedor segue-se a seguinte regra: pedra ‘quebra’ a tesoura; tesoura ‘corta’ o papel e papel
‘embrulha’ a pedra. Se ambas escolhem a mesma, há empate.
Este jogo também chama-se Joquempô, jo-quem-pô.
Sabendo como funciona o jogo crie uma variável para cada jogador que deve armazenar a opção escolhida
pela criança (Pedra, Papel ou Tesoura) e apresente o resultado da jogada
'''

import random

#exercicio 1
dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
print("====JOGO DOS DADOS====")
aposta = int(input("Faça sua aposta: "))
resultado = dado1+dado2
if aposta == resultado:
    print("Parabéns! Você acertou o número e ganhou o dinheiro!")
else:
    print("Vish.... parece que você errou! O resultado sorteado foi", resultado)

#exercicio 2
print("\n====PAR OU IMPAR====")
jogador = input("par ou ímpar? R: ").lower()

if jogador == 'par':
    maquina = 'impar'
elif jogador == 'impar':
    maquina = 'par'
else:
    print("Opção Inválida!")
    exit()
    
maquinaJogada = random.randint(0,10)
jogadorJogada = int(input("Sua jogada (0 a 10): "))
print("Valor jogado pela máquina: ", maquinaJogada)
if (maquinaJogada + jogadorJogada) % 2 == 0:
    if jogador == 'par':
        print("A soma dos valores é Par, portanto o vencedor é o jogador")
    else:
        print("A soma dos valores é Par, portanto o vencedor é a maquina")
elif maquina == 'impar':
    print("A soma dos valores é Impar, portanto o vencedor é a máquina")
else:
    print("A soma dos valores é Impar, portanto o vencedor é o jogador")

#exercicio 3
print("\n====PEDRA PAPEL OU TESOURA====")
crianca = input("Pedra, Papel ou Tesoura? R:").lower()
opcoes = ["pedra", "papel", "tesoura"]
maquina = random.randint(0,2)
if opcoes[maquina] == crianca:
    print("Empate")
    exit()
#treinando match
elif crianca not in opcoes:
    print("Opção inválida!")
    exit()
match crianca:
    case 'papel':
        if opcoes[maquina] == 'tesoura':
            print("Máquina jogou tesoura e vence a partida!")
        else:
            print("Jogada da máquina:", opcoes[maquina])
            print("Parabéns, você venceu a partida!")
    case 'tesoura':
        if opcoes[maquina] == 'pedra':
            print("Máquina jogou pedra e vence a partida!")
        else:
            print("Jogada da máquina:", opcoes[maquina])
            print("Parabéns, você venceu a partida!")
    case 'pedra':
        if opcoes[maquina] == 'papel':
            print("Máquina jogou papel e vence a partida!")
        else:
            print("Jogada da máquina:", opcoes[maquina])
            print("Parabéns, você venceu a partida!")

    
