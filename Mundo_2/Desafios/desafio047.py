"""
crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50
"""
from colorama import Fore, init

print(f"{Fore.CYAN}{'Desafio 47':=^50}")
print(f"{Fore.CYAN}{' CONTAGEM DE PARES ':=^50}")

# Começa no 2, vai até o 51 (para mostrar o 50) e pula de 2 em 2
for c in range(2, 51, 2):
    print(c, end=' ')  # O end=' ' coloca tudo na mesma linha para não poluir o terminal

print(f"\n{Fore.YELLOW}{' FIM ':=^50}")