#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

# ==============================================================
# DESAFIO 019: SORTEANDO UM ITEM NA LISTA
# ==============================================================
import random # Importa a biblioteca para gerar aleatoriedade

print(f"{' Desafio 019 ':=^50}")

# 1. ENTRADA DE DADOS
# Lendo os nomes dos alunos pelo teclado
n1 = str(input('Primeiro aluno: ')).title()
n2 = str(input('Segundo aluno: ')).title()
n3 = str(input('Terceiro aluno: ')).title()
n4 = str(input('Quarto aluno: ')).title()

# 2. CRIAÇÃO DA LISTA
# No Python, uma lista é delimitada por colchetes [ ].
lista = [n1, n2, n3, n4]

# 3. SORTEIO (PROCESSAMENTO)
# A função 'choice' escolhe aleatoriamente UM elemento da lista.
escolhido = random.choice(lista)

# 4. SAÍDA
print(f'O aluno escolhido foi: {escolhido}')

# -----------------------------------------------------------
# EXPLICAÇÃO PARA O SEU ESTUDO:
# -----------------------------------------------------------
# - LISTAS: São coleções de dados. No seu código original, você
#   criou uma lista fixa. Aqui, criamos uma dinâmica com inputs.
# - random.choice(lista): Imagine que a lista é uma sacola com
#   papéis dobrados; essa função coloca a mão na sacola e tira um.
# -----------------------------------------------------------
# EXPLICAÇÃO TÉCNICA DO .title()
# -----------------------------------------------------------
# - O método .title() é um manipulador de strings.
# - Ele transforma "ana maria" em "Ana Maria".
# - Isso evita que o seu programa exiba nomes de forma amadora se
#   o usuário for preguiçoso na digitação.
# ==============================================================