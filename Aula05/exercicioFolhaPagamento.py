print("\n\n ***** Programa para Cálculo da Folha de Pagamento ***** \n\n\n")

#ENTRADAS
horas = int(input("Qtde de horas trabalhadas no mes? "))
valor = float(input("Valor da hora de trabalho? "))

#PROCESSAMENTO
sal_bruto = horas *valor
des_sind = sal_bruto *0.03
fgts = sal_bruto*0.11
des_ir = 0

if sal_bruto > 2500:
    des_ir = sal_bruto *0.2
elif sal_bruto > 1500:
    des_ir = sal_bruto *0.1
elif sal_bruto > 900:
    des_ir = sal_bruto *0.05

#SAIDAS

#Relatorio da Folha de Pagamento

print("\n\n\n========== FOLHA DE PAGAMENTO ==========")
print("\nSalário Bruto: R$", sal_bruto)

print("\nDescontos: ")
print("* Sindicato: R$", des_sind)
print("* IR: R$", des_ir)

print("\n\n* FGTS: R$", fgts)

print("\t\t\tSalário Líquido: R$", sal_bruto-des_ir-des_sind)
print("===============================================")
