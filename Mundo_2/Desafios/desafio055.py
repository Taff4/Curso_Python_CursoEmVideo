"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
from colorama import init, Fore

init(autoreset=True)

print(f"{Fore.CYAN}{' DESAFIO 055: MAIOR E MENOR PESO ':=^50}")

maior = 0
menor = 0

for c in range(1, 6):
    while True:
        try:
            peso = float(input(f'Peso da {c}ª pessoa (kg): '))
            if peso > 0:
                break
            print(f'{Fore.RED}Erro! O peso deve ser maior que 0.')
        except ValueError:
            print(f'{Fore.RED}ERRO! Digite um peso válido.')

    # LÓGICA DE COMPARAÇÃO
    if c == 1:
        # Na primeira volta, o primeiro peso é o maior e o menor
        maior = peso
        menor = peso
    else:
        # Nas voltas seguintes, verificamos se o peso atual quebra os recordes
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"\n{Fore.GREEN}O MAIOR peso lido foi de {maior:.1f}kg.")
print(f"{Fore.YELLOW}O MENOR peso lido foi de {menor:.1f}kg.")
print(f"{Fore.CYAN}{'=' * 50}")