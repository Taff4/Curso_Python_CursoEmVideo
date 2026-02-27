# ==============================================================
# CURSO PYTHON #08 - MÓDULOS E BIBLIOTECAS EXTERNAS
# ==============================================================

# 1. BIBLIOTECAS INTERNAS (Vêm com o Python)
# -----------------------------------------------------------
import math   # Traz tudo da matemática
import random # Traz tudo de geração aleatória

# 2. BIBLIOTECAS EXTERNAS (Precisam ser instaladas)
# -----------------------------------------------------------
# Como instalar: Vá no terminal do PyCharm e digite: pip install emoji
import emoji

# -----------------------------------------------------------
# EXPLICAÇÕES TÉCNICAS (CONSOLIDADO):
# -----------------------------------------------------------
"""
- BIBLIOTECA PADRÃO: É como o app de SMS do celular, já vem nele.
- BIBLIOTECA EXTERNA: É como o Instagram, você precisa baixar (via PIP).
- COMANDO IMPORT: Traz a biblioteca inteira (Ex: import bebida).
- FROM IMPORT: Traz um item específico (Ex: from doce import pudim).
"""

# --- PRÁTICA 1: RANDOM ---
# Gera um número inteiro aleatório entre 1 e 10
num_sorte = random.randint(1, 10)

# --- PRÁTICA 2: MATH (Exemplo do Vídeo) ---
# Usando a forma 'from' para importar itens específicos
from math import sqrt, floor

num_usuario = int(input('Digite um número para ver a raiz: '))
raiz = sqrt(num_usuario)

# --- SAÍDA DE DADOS ---
print(f'\nO número da sorte gerado foi: {num_sorte}')
print(f'A raiz de {num_usuario} é {floor(raiz)}') # floor arredonda para baixo

# --- PRÁTICA 3: EMOJI (Biblioteca Externa) ---
# O comando emojize converte o código de texto em ícone
print(emoji.emojize('Olá Mundo! :earth_americas:', language='alias'))
print(emoji.emojize('Python é foda! :snake:', language='alias'))

# ==============================================================
# DICA DE ESTUDO:
# Se o 'import emoji' estiver com uma linha vermelha, o PyCharm
# vai te oferecer uma lâmpada vermelha. Clique nela e selecione
# "Install package emoji" para ele instalar sozinho!