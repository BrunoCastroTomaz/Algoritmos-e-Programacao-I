amigo = []
def menu():
    print("1) Cadastrar um amigo (no início da lista)")
    print("2) Mostrar o nome de todos os amigos")
    print("3) Cadastrar um amigo (no final da lista)")
    print("4) Remover um nome")
    print("5) Substituir um nome")
    print("6) Mostrar o número total de amigos cadastrados")
    print("7) Colocar nomes dos amigos em ordem alfabética")
    print("8) Sair do Programa")
    op = int(input("Opção selecionada: "))
    while op <1 or op >8:
        op = int(input("Opção selecionada: "))
    return op
def inserir_amigo():
    nome = input("Digite um nome: ")
    amigo.insert(0,nome)
def mostrar_nomes():
    print(amigo)
def inserir_amigo_final():
    nome = input("nome: ")
    amigo.append(nome)
def remover_amigo():
    nome = input("digite o nome a ser removido: ")
    for i in range(0,len(amigo)):
        if amigo[i] == nome:
            pos = i
            break
    del amigo[pos]
def substituir_nome():
    nome = input("Qual o nome a ser substituido? R: ")
    nomenovo = input("Qual o novo nome: ")
    for i in range(0,len(amigo)):
        if amigo[i] == nome:
            amigo[i] = nomenovo
            break
def total_cadastro():
    print("Total de amigos = %d" %len(amigo))
def ordenar_amigos():
    amigo.sort()
    mostrar_nomes()
def main():
    amigo = []
    while True:
        op = menu()
        if op ==1:
            inserir_amigo()
        elif op == 2:
            mostrar_nomes()
        elif op == 3:
            inserir_amigo_final()
        elif op == 4:
            remover_amigo()
        elif op == 5:
            substituir_nome()
        elif op == 6:
            total_cadastro()
        elif op == 7:
            ordenar_amigos()
        if op == 8:
            break
main()
