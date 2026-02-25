print(F"{'Desafio 012' :=^50}")

#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

# Entrada
preco = float(input('Qual é o preço do produto? R$ '))

# Cálculo 
desconto = preco * 5 / 100
novo_preco = preco - desconto

# Saída com formatação de 2 casas decimais
print('O produto que custava R${:.2f}, na promoção de 5% vai custar R${:.2f}.'.format(preco, novo_preco))
print('Você economizou R${:.2f}!'.format(desconto))

#Por que usar * 5 / 100 em vez de * (5/100)?
#No Python, a multiplicação e a divisão têm a mesma prioridade e são resolvidas da esquerda para a direita. Usar preco * 5 / 100 é o padrão mais comum e dispensa os parênteses, deixando o código mais limpo.