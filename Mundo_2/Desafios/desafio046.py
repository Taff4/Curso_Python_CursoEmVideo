"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifico, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""

from colorama import Fore, init
from time import sleep

init(autoreset=True)

print(f"{Fore.CYAN}{'Desafio 46':=^50}")
print(f"{Fore.CYAN}{' CONTAGEM REGRESSIVA ':=^50}")

# Lógica correta:
# Começa em 10, vai até o -1 (para mostrar o 0) e tira 1 a cada volta (-1)
for c in range(10, -1, -1):
    print(f"{Fore.RED}{c}")
    sleep(1)

# Efeito final para os fogos
print(f"{Fore.YELLOW}{' BUM! BUM! POOOW! 🎆 ':=^50}")