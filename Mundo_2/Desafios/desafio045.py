"""
Crie um programa que faça o computador jogar jokenpô po
"""

from colorama import Fore, init
from random import randint
from time import sleep

init(autoreset=True)

# Itens do jogo (O computador escolherá um índice desta lista)
itens = ('Pedra', 'Papel', 'Tesoura')

print(f"{Fore.MAGENTA}{' JOKENPÔ ':=^50}")

# 1. ESCOLHA DO COMPUTADOR
computador = randint(0, 2)

# 2. ENTRADA DO JOGADOR COM VALIDAÇÃO
while True:
    try:
        print('''Suas opções:
        [ 0 ] PEDRA
        [ 1 ] PAPEL
        [ 2 ] TESOURA''')
        jogador = int(input('Qual é a sua jogada? '))

        if 0 <= jogador <= 2:
            break
        else:
            print(f"{Fore.RED}OPÇÃO INVÁLIDA! Escolha entre 0, 1 ou 2.")
    except ValueError:
        print(f"{Fore.RED}ERRO: Digite apenas o número da sua jogada.")

# 3. EFEITO DRAMÁTICO (SLEEP)
print(f"{Fore.YELLOW}JO...")
sleep(1)
print(f"{Fore.YELLOW}KEN...")
sleep(1)
print(f"{Fore.YELLOW}PÔ!!!")

# 4. MOSTRANDO AS JOGADAS
print(f"{Fore.CYAN}{'='*25}")
print(f"Computador jogou: {Fore.WHITE}{itens[computador]}")
print(f"Jogador jogou: {Fore.WHITE}{itens[jogador]}")
print(f"{Fore.CYAN}{'='*25}")

# ------------------------------------------------------------------------------
# 5. LÓGICA DE QUEM VENCEU
# ------------------------------------------------------------------------------
if computador == 0:  # Computador jogou PEDRA
    if jogador == 0:
        print(f"{Fore.YELLOW}EMPATE!")
    elif jogador == 1:
        print(f"{Fore.GREEN}JOGADOR VENCE!")
    elif jogador == 2:
        print(f"{Fore.RED}COMPUTADOR VENCE!")

elif computador == 1:  # Computador jogou PAPEL
    if jogador == 0:
        print(f"{Fore.RED}COMPUTADOR VENCE!")
    elif jogador == 1:
        print(f"{Fore.YELLOW}EMPATE!")
    elif jogador == 2:
        print(f"{Fore.GREEN}JOGADOR VENCE!")

elif computador == 2:  # Computador jogou TESOURA
    if jogador == 0:
        print(f"{Fore.GREEN}JOGADOR VENCE!")
    elif jogador == 1:
        print(f"{Fore.RED}COMPUTADOR VENCE!")
    elif jogador == 2:
        print(f"{Fore.YELLOW}EMPATE!")

print(f"{Fore.MAGENTA}{'='*50}")