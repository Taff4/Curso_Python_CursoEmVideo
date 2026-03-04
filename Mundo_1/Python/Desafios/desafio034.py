#Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento
#para salarios superiores a 1259, calcule um aumento de 10%
#para o salario inferiores ou iguais, o aumento é de 15%

print(f"{' DESAFIO 034 ':=^50}")

# 1. Entrada
salario = float(input('Qual é o salário do funcionário? R$'))

# 2. Lógica de Aumento
# Calculamos apenas a porcentagem dentro do IF/ELSE
if salario > 1250:
    porcentagem = 10
else:
    porcentagem = 15

# 3. Cálculo fora da condição (para não repetir código)
aumento = salario * (porcentagem / 100)
novo_salario = salario + aumento

# 4. Saída formatada
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${novo_salario:.2f}.')
print(f'Um aumento real de {porcentagem}% (R${aumento:.2f} a mais).')