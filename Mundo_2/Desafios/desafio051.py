"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""
from colorama import Fore, init

init(autoreset=True)

print(f"{Fore.CYAN}{' DESAFIO 051: PROGRESSÃO ARITMÉTICA ':=^50}")

# 1. ENTRADA DE DADOS
while True:
    try:
        primeiro = int(input("Primeiro termo: "))
        razao = int(input("Razão da PA: "))
        break
    except ValueError:
        print(f'{Fore.RED}ERRO! Digite um número inteiro válido.')

print(f"\nOs 10 primeiros termos dessa PA são:")
print(f"{Fore.YELLOW}=", end="")

# 2. LÓGICA DA PA
# Usando o seu raciocínio: i vai de 0 até 9
for i in range(0, 10):
    termo = primeiro + (i * razao)
    print(f" {termo} ", end="→")

print(f" {Fore.RED}ACABOU")
print(f"{Fore.YELLOW}=" * 50)

"""
Existe uma segunda forma de fazer isso usando o próprio range para saltar. O Python permite que o range use a razão como o "passo" (step):

decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f"{c}", end=" → ")

Ambas as formas estão certas! COM i é excelente porque não precisa calcular o decimo termo antes de começar.
"""