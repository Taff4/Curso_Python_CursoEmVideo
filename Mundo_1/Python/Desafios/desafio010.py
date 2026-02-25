print(f"{'Desafio 010' :=^50}")

#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar considere o valor do dolar em relação ao real

# Entrada de dados
real = float(input('Quanto dinheiro você tem na carteira? R$'))

# Cálculo (considerando a cotação que você escolheu)
cotacao = 5.15
dolar = real / cotacao

# Exibição formatada
print('Com R${:.2f}, você pode comprar US${:.2f}'.format(real, dolar))

# R${:.2f}: O R$ aparece antes do número, e o :.2f garante que o valor apareça como 20.00 em vez de 20.0.

# US${:.2f}: Mesma coisa para o dólar. Se você tiver R$ 10,00, o resultado será US$ 1.94\ em vez daquela dízima enorme.