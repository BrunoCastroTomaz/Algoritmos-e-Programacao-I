'''

'''

cliente = input("Por favor insira o seu nome: ")
print("A tabela abaixo indica o código correspondente para cada região\n")
print("Região\tCódigo\nSul\t1\nNorte\t2\nLeste\t3\nOeste\t4\n")
codigo = int(input("Digite o código da sua região:"))
vendedor = input("Ótimo! Agora escreva o nome do vendedor: ")
num_pecas = int(input("Obrigado! Forneça o número de peças vendidas:"))

if codigo == 1 and num_pecas <= 1000 :
   caso = 1.00
if codigo == 1 and num_pecas > 1000:
   caso = 0.90
if codigo == 2 and num_pecas <= 1000:
   caso = 1.10
if codigo == 2 and num_pecas > 1000:
   caso = 1.00
if codigo == 3 and num_pecas <= 1000:
   caso = 1.15
if codigo == 3 and num_pecas > 1000:
   caso = 1.10
if codigo == 4 and num_pecas <= 1000:
   caso = 1.20
if codigo == 4 and num_pecas >  1000:
   caso = 1.15

custo_total = 7.00 * num_pecas
frete  = num_pecas * caso
print("O valor do frete deve ser ", frete)
vl_total_venda = custo_total + custo_total / 2
vl_comissao_vendedor = 6.5 * vl_total_venda /100
print("A comissão do vendedor é de: ",vl_comissao_vendedor)
lucro = vl_total_venda - vl_comissao_vendedor - custo_total
print("O lucro obtido com a venda é de ",lucro)
