#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.

print(f"{'Desafio 027' :=^50}")

# 1. Entrada: .title() já deixa as primeiras letras maiúsculas (ex: Ana Maria)
nome = str(input('Digite seu nome completo: ')).strip().title()

# 2. Lógica:
# O .split() transforma o nome em uma lista de palavras
palavras = nome.split()

# Primeiro nome: Índice 0
f_nome = palavras[0]

# Último nome: Índice -1 (O Python começa a contar de trás para frente!)
l_nome = palavras[-1]
#saida
print(f'Seu nome completo é: {nome}')
print(f'Primeiro nome {f_nome}')
print(f'ultimo nome {l_nome}')