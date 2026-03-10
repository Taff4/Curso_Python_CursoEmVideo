# ==============================================================================
#          BIBLIOTECA MESTRA: ESTRUTURAS DE REPETIÇÃO (LAÇO FOR)
# ==============================================================================
# Este script serve como material de apoio para os desafios 046 ao 056.
# Use como base para entender a sintaxe e a lógica de iteração.

"""
📌 REGRAS DE OURO DO RANGE (O CORAÇÃO DO FOR):

1. O ÚLTIMO NÚMERO É EXCLUSIVO:
   range(1, 10) -> O Python para no 9. Ele SEMPRE ignora o limite final.
   SOLUÇÃO: Use (fim + 1) para incluir o número desejado.

2. A VARIÁVEL DE CONTROLE:
   'for c in range...' -> O 'c' nasce aqui e muda a cada volta. 
   Pode ser qualquer nome: i, p, item, cont, passo.

3. INDENTAÇÃO (4 ESPAÇOS):
   O que está recuado REPETE. 
   O que está alinhado ao 'for' executa APENAS UMA VEZ ao final do laço.
"""

# ------------------------------------------------------------------------------
# 1. EXEMPLOS DE CONTAGEM (SINTAXE BÁSICA)
# ------------------------------------------------------------------------------

# CONTAGEM CRESCENTE (0 a 5)
for c in range(0, 6): 
    print(c) 

# CONTAGEM REGRESSIVA (Para trás)
# O segredo é o '-1' no final (a iteração negativa)
for c in range(6, 0, -1): 
    print(c) 

# PULANDO NÚMEROS (Step/Passo)
# O terceiro parâmetro define o intervalo. Ex: de 2 em 2.
for c in range(0, 7, 2): 
    print(c)

# ------------------------------------------------------------------------------
# 2. INTERAÇÃO COM O USUÁRIO (DINÂMICO)
# ------------------------------------------------------------------------------

# CONTAR ATÉ ONDE O USUÁRIO QUISER (+1 para incluir o número)
n = 10 # Simulação de input
for c in range(0, n + 1): 
    print(c)

# CONTROLE TOTAL (Início, Fim e Passo)
i = 1  # Início
f = 10 # Fim
p = 2  # Passo
for c in range(i, f + 1, p): # Lê o início, vai até o fim, pulando o passo
    print(c)

# ------------------------------------------------------------------------------
# 3. ACUMULADORES E CONTADORES (ESSENCIAL PARA DESAFIOS)
# ------------------------------------------------------------------------------

# O SOMATÓRIO (Acumulador)
s = 0 # IMPORTANTE: Começa em 0 fora do laço
for c in range(0, 3):
    num = 5 # Simulação de input
    s += num # s recebe ele mesmo + o novo número (s = s + num)
print(f'O somatório final foi {s}')

# O CONTADOR (Contar quantas vezes algo acontece)
cont = 0
for c in range(1, 11):
    if c % 2 == 0: # Se o número for par
        cont += 1  # Adiciona 1 ao contador
print(f'Foram encontrados {cont} números pares.')

# ------------------------------------------------------------------------------
# 4. TRUQUES DE FORMATAÇÃO NO TERMINAL
# ------------------------------------------------------------------------------

# TUDO NA MESMA LINHA: Use o parâmetro end=' '
for c in range(0, 5):
    print(c, end=' - ')
# Resultado: 0 - 1 - 2 - 3 - 4 -

# PAUSA DRAMÁTICA: Use o sleep (Necessário: from time import sleep)
# for c in range(5, 0, -1):
#     print(c)
#     sleep(1) # Espera 1 segundo antes da próxima volta

# ------------------------------------------------------------------------------
# 5. DICAS DE "BLINDAGEM" (TRY/EXCEPT)
# ------------------------------------------------------------------------------
# Sempre que usar inputs dentro ou antes do FOR, envolva em um try/except
# para evitar que o programa trave se o usuário digitar letras.
"""
while True:
    try:
        vezes = int(input('Quantas vezes repetir? '))
        break
    except ValueError:
        print('Erro! Digite um número inteiro.')
"""

# ==============================================================================
# PRÓXIMOS PASSOS: 
# Desafio 046 (Fogos) -> Use Contagem Regressiva e Sleep.
# Desafio 047 (Pares) -> Use Range com Step 2.
# Desafio 048 (Soma ímpares) -> Use Acumulador e IF.
# ==============================================================================