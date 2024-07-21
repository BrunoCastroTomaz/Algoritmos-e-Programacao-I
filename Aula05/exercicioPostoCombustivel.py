'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
• até 20 litros, desconto de 3% por litro
• acima de 20 litros, desconto de 5% por litro
Gasolina:
• até 20 litros, desconto de 4% por litro
• acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da
seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se
que o preço do litro da gasolina é R$ 5,50 o preço do litro do álcool é R$ 3,90.
'''
#Ellipsis
litros =float(input("Informe a qtde de litros utilizado no abastecimento: "))
tipoCombustivel = input("Informe o tipo de combustível (A - álcool ou G - gasolina): ").upper()

#PROCESSAMENTO
if tipoCombustivel == 'A' and litros <= 20:
    print("Combustível utilizado: Alcool")
    valorPago = (litros*3.90) - (litros*3.90)*0.03
    print("Valor a pagar: R$", valorPago)
elif tipoCombustivel == 'A' and litros > 20:
    print("Combustível utilizado: Alcool")
    valorPago = (litros*3.90) - (litros*3.90)*0.05
    print("Valor a pagar: R$", valorPago)
elif tipoCombustivel == 'G' and litros <= 20:
    print("Combustível utilizado: Gasolina")
    valorPago = (litros*5.50) - (litros*3.90)*0.04
    print("Valor a pagar: R$", valorPago)
elif tipoCombustivel == 'G' and litros > 20:
    print("Combustível utilizado: Gasolina")
    valorPago = (litros*5.50) - (litros*3.90)*0.06
    print("Valor a pagar: R$", valorPago)
    
