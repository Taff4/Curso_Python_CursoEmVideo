"""
"Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o."
"""
from colorama import Fore, init

init(autoreset=True)
print(f"{Fore.CYAN}{' DESAFIO 050: SOMA DOS PARES ':=^50}")

soma = 0
cont = 0  # Dica: é legal contar quantos pares foram somados também!

for c in range(1, 7):
    while True:
        try:
            num = int(input(f'Digite o {c}º valor: '))
            break
        except ValueError:
            print(f'{Fore.RED}ERRO! Digite um número inteiro válido.')

    # Lógica: Se o número for par, acumula
    if num % 2 == 0:
        soma += num # soma = soma + num
        cont += 1 # cont = cont + 1

# Exibição final FORA do laço for
print(f"{Fore.CYAN}{'=' * 50}")
if cont > 0:
    print(f"Você digitou {cont} números PARES e a soma foi: {Fore.GREEN}{soma}")
else:
    print(f"{Fore.YELLOW}Você não digitou nenhum número par para somar.")