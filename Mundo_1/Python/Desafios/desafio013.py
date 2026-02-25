print(f"{'Desafio 013' :=^50}")

#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

#Entrada
salario = float(input('Qual é seu salário? R$ '))

#Cálculo
aumento = salario * 15 / 100
novo_salario = salario+aumento

#Saída

print('O seu salário era R${:.2f}. Com R${:.2f} de aumento, vai passar para R${:.2f}.'.format(salario, aumento, novo_salario))

#Na matemática e na programação, quando queremos dar um aumento, podemos multiplicar direto pelo fator.

#Se o aumento é de 15%, o novo valor é 115% do original.

# Logo, você pode fazer: novo_salario = salario * 1.15