#Python tem suporte a parametros nomeados, ambas as opções abaixo produzem o mesmo resultado
# isso permite que os parâmetros passados na chamada da função não precisam estar na mesma ordem (dessa forma a ordem não importa)

'''
def calculo_imc(peso, altura):
    print(peso / altura ** 2)

calculo_imc(peso = 75, altura = 1.68)
'''

def calculo_imc(peso, altura):
    print(peso / altura ** 2)

calculo_imc(75, 1.68)


#função embutida (builtin) max() que retorna o maior valor de uma lista
maior_numero = max(1, 2, 3)
maior_letra = max('a', 'b', 'c') #tabela ASCII
print(maior_numero)
print(maior_letra)

#essa função não faz nada
def foo():
    pass
'''
A instrução “pass” é usada para indicar que nenhuma ação deve ser tomada no loop e
que o loop deve continuar normalmente. A instrução “pass” é útil quando o programa
ainda não possui uma implementação completa para uma determinada parte do código,
mas precisa que o código seja compilado e executado sem erros.
'''

#imprime 30 underlines
def linha():
    print("_"*30)
linha()
