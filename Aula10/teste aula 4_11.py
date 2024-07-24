#codigo recebe 10 numeros, adiciona-os em uma lista e imprime a lista em ordem inversa
lst=[]
print ("escreve os números: ")
for i in range(10):
    lst.append(input())
lst.reverse()
print(lst)

#operações em lista

lista = [1, 'a', ['ab', 'CD']]
#criacao de lista
print("\nCRIAR")
print("Exibindo a lista: ", lista)

#recuperando (retrieve) um elemento
print("\nRECUPERAR(retrieve)")
print("Elemento na posição de índice 2: ", lista[2])

#substituir (replace)
print("\nSUBSTITUIR (replace)")
print("Antes: ", lista)
lista[2] = "substituirItem"
print("Depois - substituiu (ab, CD): ", lista)

#inserir (insert)
print("\nINSERIR (insert)")
print("Antes: ", lista)
lista.insert(2,"inserirElemPos2") #nao sobrescreve
print("Depois: ", lista)

#remover/apagar
print("\nREMOVER")
print("Antes: ", lista)
del lista[0]
print("Depois-apagou(1): ", lista)

#acrescentar (append/último)
print("\nACRESCENTAR ÚLTIMO/append")
print("Antes: ", lista)
lista.append("ultimo")
print("Depois-acrescentou último item: ", lista)

#ordenar crescente (sort)
print("\nORDENAR CRESCENTE")
print("Antes: ", lista)
lista.sort()
print("Depois-ordenado crescente: ", lista)
