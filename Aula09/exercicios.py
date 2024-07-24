'''
Faça uma função que recebe, por parâmetro, a altura em metros (alt) e o sexo de uma
pessoa e retorna o seu peso ideal. Para homens, calcular o peso ideal usando a fórmula:
peso ideal = 72.7 x alt - 58 e, para mulheres, peso ideal = 62.1 x alt - 44.7. Considere uma
casa após a virgula apenas.
'''
altura=float(input('Insira a altura (metros): '))
sexo=str(input('Insira o sexo:m/f ')).upper()

def peso(x):
    if sexo=='M':
        return(72.7*x)-58
    else:
        return(62.1*x)-44.7

total=peso(altura)
print("%.1f" %total)

'''
Escreva um procedimento que receba um número inteiro e imprima o mês correspondente
ao número. Por exemplo, 2 corresponde à “fevereiro”. O procedimento deve mostrar uma
mensagem de erro caso o número recebido não faça sentido. Gere também um algoritmo
que leia um valor como entrada do usuário e chame o procedimento criado
'''
meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
def mes(numero):
    if numero < 1 or numero > 12:
        print("Esse mês nem existe!")
    else:
        print(meses[numero-1])
escolheMes = int(input("Fala um número de mês meu compadre: "))
mes(escolheMes)


'''
Criar uma função que determine se um caractere, recebido como parâmetro, é ou não uma
letra do alfabeto. A função deve retornar 1 caso positivo e 0 em caso contrário. Escreva
também um algoritmo para testar tal função
'''
def isCaracter(caracter):
    if caracter.isalpha():
        return 1
    else:
        return 0
c = input("Fala um caracter: ")
print(isCaracter(c))

'''
Crie uma função que realize a conversão de pés (feet) para metros (m), onde feet é passado
como parâmetro e m é retornado. Sabe-se que 1 metro está para 3,281 pés. Crie também
um algoritmo para testar tal função
'''
def convertefeet(feet):
    return feet/3.281
feet = float(input("Qtos pes? R: "))
print("Equivale a", convertefeet(feet), " metros")


