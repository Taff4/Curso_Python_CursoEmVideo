# ==============================================================================
#             AULA 11: CORES NO TERMINAL (PADRÃO ANSI) - PYCHARM
# ==============================================================================

"""
A sequência de escape ANSI sempre começa com \033[ e termina com m.
A estrutura interna é: \033[ STYLE ; TEXT ; BACK m

[TABELA DE REFERÊNCIA RÁPIDA]
STYLE: 0 (Normal), 1 (Negrito), 4 (Sublinhado), 7 (Invertido/Negative)
TEXT:  30 (Branco), 31 (Vermelho), 32 (Verde), 33 (Amarelo), 34 (Azul), 35 (Roxo), 36 (Ciano), 37 (Cinza)
BACK:  40 a 47 (Segue a mesma ordem do texto, mas para o fundo)
"""

# --- EXEMPLOS DIRETOS ---
# Fundo Roxo, Texto Branco, Sublinhado
print('\033[4;30;45m Olá, mundo! \033[m')

# Fundo Azul, Texto Amarelo
print('\033[0;33;44m Olá, mundo! \033[m')

# Invertido (O que era fundo vira texto e vice-versa)
print('\033[7;33;44m Olá, mundo! \033[m')

print('-' * 40)

# --- USO COM VARIÁVEIS (f-strings) ---
a = 3
b = 5
# Note que abrimos a cor antes da {variável} e fechamos com \033[m logo depois
print(f'Os valores são \033[32m{a}\033[m e \033[34m{b}\033[m')

print('-' * 40)

# --- MÉTODO PROFISSIONAL: DICIONÁRIO DE CORES ---
# Esta é a melhor forma de organizar seus códigos no PyCharm para não precisar
# decorar os números toda vez que quiser usar uma cor.

cores = {
    'limpa':        '\033[m',
    'branco':       '\033[30m',
    'vermelho':     '\033[31m',
    'verde':        '\033[32m',
    'amarelo':      '\033[33m',
    'azul':         '\033[34m',
    'roxo':         '\033[35m',
    'ciano':        '\033[36m',
    'cinza':        '\033[37m',
    'pretoebranco': '\033[7;30m'
}

# Aplicando o dicionário:
print(f"Olá! Muito {cores['verde']}prazer{cores['limpa']} em te conhecer!")
print(f"Este é um teste de {cores['vermelho']}ERRO{cores['limpa']} em vermelho.")
print(f"E este é um teste {cores['pretoebranco']} INVERTIDO {cores['limpa']}.")

# ==============================================================================
# DICA PRO: No PyCharm, use Ctrl+Alt+L para formatar seu dicionário e deixá-lo
# bem alinhado como este acima!