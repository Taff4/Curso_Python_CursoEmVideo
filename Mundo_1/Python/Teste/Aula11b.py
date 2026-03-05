# ==============================================================================
#                 DOMINANDO O MÓDULO COLORAMA (GUIA DEFINITIVO)
# ==============================================================================

# 1. A IMPORTAÇÃO:
# Fore  -> Altera a cor da FONTE (letras)
# Back  -> Altera a cor do BACKGROUND (fundo)
# Style -> Altera o ESTILO (negrito, brilho, reset)
# init  -> É a função que "liga" o sistema de cores
from colorama import Fore, Back, Style, init

# 2. O COMANDO MÁGICO (init):
# autoreset=True -> Isso é OBRIGATÓRIO para iniciantes.
# Ele faz com que a cor pare EXATAMENTE onde a string acaba.
# Se você não usar isso, o seu terminal continuará colorido mesmo após o print.
init(autoreset=True)

print(f"{Style.BRIGHT}--- DEMONSTRAÇÃO DE COMANDOS ---")

# ------------------------------------------------------------------------------
# 3. USANDO 'FORE' (CORES DE TEXTO)
# ------------------------------------------------------------------------------
print(Fore.RED + "Este texto é vermelho!")
print(Fore.GREEN + "Este texto é verde!")
print(Fore.BLUE + "Este texto é azul!")
print(Fore.YELLOW + "Este texto é amarelo!")
print(Fore.MAGENTA + "Este texto é roxo (magenta)!")
print(Fore.CYAN + "Este texto é ciano (azul bebê)!")

# ------------------------------------------------------------------------------
# 4. USANDO 'BACK' (CORES DE FUNDO)
# ------------------------------------------------------------------------------
print(Back.WHITE + Fore.BLACK + "Texto preto com fundo branco!")
print(Back.RED + Fore.YELLOW + "Texto amarelo com fundo vermelho!")

# ------------------------------------------------------------------------------
# 5. USANDO 'STYLE' (ESTILOS)
# ------------------------------------------------------------------------------
# Style.BRIGHT -> Deixa a cor viva e em negrito
# Style.DIM    -> Deixa a cor opaca, mais escura (cinza)
# Style.NORMAL -> Volta ao padrão do sistema
print(Style.BRIGHT + Fore.GREEN + "Verde Brilhante (Negrito)")
print(Style.DIM + Fore.GREEN + "Verde Opaco (Fosco)")

# ------------------------------------------------------------------------------
# 6. DICA PRO: USANDO DENTRO DE F-STRINGS (O mais prático no dia a dia)
# ------------------------------------------------------------------------------
nome = "Rafael"
status = "APROVADO"

# Note como injetamos a cor direto na frase:
print(f"Olá {Fore.CYAN}{nome}{Style.RESET_ALL}! Seu status é {Back.GREEN}{Fore.WHITE} {status} ")

# ==============================================================================
# POR QUE ISSO É MELHOR QUE O \033[...]?
# 1. Legibilidade: Você lê "Fore.RED" e já sabe que é vermelho.
# 2. Manutenção: É muito mais fácil trocar Fore.RED por Fore
print(f'{'-':=^50}')

from colorama import Fore, Back, Style, init
init(autoreset=True)

# --- PADRÃO DE CORES DO CURSO ---
TITULO = Back.BLUE + Fore.WHITE + Style.BRIGHT
SUCESSO = Fore.GREEN + Style.BRIGHT
ERRO = Fore.RED + Style.BRIGHT
ALERTA = Fore.YELLOW
RESET = Style.RESET_ALL

# Exemplo de uso:
print(f"{TITULO}  BANCO CEV  ")
print(f"Status: {SUCESSO}APROVADO")