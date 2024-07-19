n1 = int(input())
n2 = int(input())
print('A soma entre {0} e {1} é {2}'.format(n1,n2,n1+n2))

n3 = bool(input()) #se nao houver input imprime false
print(n3)

m = input()
print(m.isnumeric()) #verifica se o m é um numero (ou se é possível converter a string de input em um numero)

n = input()
print(n.isalpha()) #verifica se é caracter do alfabeto

o = input()
print(o.isalnum()) #verifica se é um caracter do alfabeto ou numero
print(o.isprintable()) #verifica se o valor pode ser impresso
