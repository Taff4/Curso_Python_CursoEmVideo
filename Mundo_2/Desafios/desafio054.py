"""
"Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade (21 anos) e quantas já são maiores."
"""
from colorama import init, Fore
from datetime import date

init(autoreset=True)

print(f"{Fore.CYAN}{'Desafio 54':=^50}")

atual = date.today().year # Pega o ano atual (2026)
#contador
tot_maior = 0
tot_menor = 0

for c in range(1, 8):
    while True:
        try:
            nasc = int(input(f'Em que ano a {c}ª pessoa nasceu(ex:1998)? '))
            if 1900 < nasc <= atual:
                break
            print(f'{Fore.RED}Erro! Digite um ano entre 1900 e {atual}.')
        except ValueError:
            print(f'{Fore.RED}ERRO! Digite um ano válido (números).')

    idade = atual - nasc
    # LÓGICA CORRETA: Maior ou igual a 21
    if idade >= 21:
        tot_maior += 1
    else:
        tot_menor += 1
print(f"\n{Fore.GREEN}Ao todo tivemos {tot_maior} pessoas maiores de idade.")
print(f"{Fore.YELLOW}E também tivemos {tot_menor} pessoas menores de idade.")
print(f"{Fore.CYAN}{'=' * 50}")

