#Faça um programa que leia o numero de 0 a 9999 e mostre na tela cada um dos digitos separados

print(f"{' Desafio 023 - Versão Final ':=^50}")

num = int(input('Digite um número entre 0 e 9999: '))

# A lógica correta utiliza a divisão INTEIRA (//)
# para "empurrar" o dígito para a casa da unidade
# e o MÓDULO (%) para isolar esse dígito.

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Analisando o número {num}:')
print(f'Unidade: {u}')
print(f'Dezena:  {d}')
print(f'Centena: {c}')
print(f'Milhar:  {m}')

# u = n // 1 % 10 -> O operador // remove casas decimais e o % isola o último dígito.
# .zfill(4) -> (Se usar String) Garante que números curtos como '12' virem '0012'
# evitando o erro de "índice fora de alcance" (IndexError).