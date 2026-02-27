#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

# ==============================================================
# DESAFIO 020: SORTEANDO UMA ORDEM NA LISTA
# ==============================================================
import random #

print(f"{' Desafio 020 ':=^50}")

# 1. ENTRADA DE DADOS
# Usamos .title() para capitular e .strip() para limpar espaços.
n1 = str(input('Primeiro aluno: ')).title().strip()
n2 = str(input('Segundo aluno: ')).title().strip()
n3 = str(input('Terceiro aluno: ')).title().strip()
n4 = str(input('Quarto aluno: ')).title().strip()

# 2. CRIAÇÃO DA LISTA
lista = [n1, n2, n3, n4]

# 3. EMBARALHAMENTO (PROCESSAMENTO)
# Diferente do choice, o shuffle REORDENA a própria lista original.
# Ele não retorna um valor novo, ele altera a lista que já existe.
random.shuffle(lista)

# 4. SAÍDA
print('\nA ordem de apresentação será:')
print(lista) # Exibe a lista já embaralhada.

# -----------------------------------------------------------
# EXPLICAÇÃO PARA O SEU ESTUDO:
# -----------------------------------------------------------
# - random.choice(lista): Escolhe UM (como um sorteio de prêmio).
# - random.shuffle(lista): Muda a ORDEM de todos (como embaralhar cartas).
# - Por que não funcionou o {apresentacao-1}?
#   Porque 'apresentacao' é uma palavra (String), e o Python não sabe
#   fazer conta de menos com palavras!
# ==============================================================