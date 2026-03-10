"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas mulheres têm menos de 20 anos.
"""

from colorama import init, Fore

init(autoreset=True)
print(f"{Fore.CYAN}{' DESAFIO 056: ANALISADOR COMPLETO ':=^50}")

soma_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
tot_mulher_20 = 0

for c in range(1, 5):
    print(f"\n{Fore.YELLOW}--- {c}ª PESSOA ---")

    # 1. VALIDAÇÃO DO NOME
    while True:
        nome = input(f"NOME: ").strip().upper()
        if nome and nome.replace(" ", "").isalpha():
            break
        print(f"{Fore.RED}Erro! Digite um nome válido.")

    # 2. VALIDAÇÃO DA IDADE
    while True:
        try:
            idade = int(input(f"IDADE: "))
            if 0 <= idade <= 120: break
            print(f"{Fore.RED}Idade inválida.")
        except ValueError:
            print(f"{Fore.RED}Digite um número.")

    # 3. VALIDAÇÃO DO SEXO
    while True:
        sexo = input(f"SEXO [M/F]: ").strip().upper()
        if sexo in ('M', 'F'): break
        print(f"{Fore.RED}Digite M ou F.")

    soma_idade += idade

    if sexo == 'M':
        # Se for o primeiro homem ou se este for mais velho que o anterior
        if maior_idade_homem == 0 or idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_mais_velho = nome

    if sexo == 'F' and idade < 20:
        tot_mulher_20 += 1

# === CÁLCULO FINAL (FORA DO FOR) ===
media = soma_idade / 4

print(f"\n{Fore.CYAN}{'=' * 50}")
print(f"A média de idade do grupo é de {Fore.GREEN}{media:.1f} anos.")

if nome_mais_velho == '':
    print(f"Não foram registrados homens no grupo.")
else:
    print(f"O homem mais velho tem {maior_idade_homem} anos e se chama {Fore.GREEN}{nome_mais_velho}.")

print(f"Ao todo são {Fore.GREEN}{tot_mulher_20} mulheres{Fore.RESET} com menos de 20 anos.")
print(f"{Fore.CYAN}{'=' * 50}")
