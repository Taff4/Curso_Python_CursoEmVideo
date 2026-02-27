print(f"{'Desafio 015' :=^50}")

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

#Entrada
dias_alugados = int(input('Quantos dias alugados? '))
km = float(input('Qual foi a quantidade de km rodados? '))
#Calculo
preco_km = 0.15
preco_diaria = 60.00

preco_a_pagar = (dias_alugados * preco_diaria ) + (km * preco_km)

#Saida
print('O valor total a pagar é de R${:.2f} '.format(preco_a_pagar))

