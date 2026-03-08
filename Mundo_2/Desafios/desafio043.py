"""
Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule IMC e mostre sue status, de acordo com a tabela abaixo:
#Abaixo de 18.5: abaixo do ésp
#Entre 18.5 e 25: peso ideal
# 25 até 30: sobrepeso
#30 até 40: obesidade
#acima de 40: obesidade mórbida
"""

# ==============================================================================
#           DESAFIO 043: CÁLCULO DE IMC (ÍNDICE DE MASSA CORPORAL)
# ==============================================================================
from colorama import Fore, Style, init

init(autoreset=True)

print(f"{Fore.YELLOW}{' DESAFIO 43 ':=^50}")
print(f"{Fore.YELLOW}{' ANALISADOR DE IMC ':=^50}")

# 1. ENTRADA COM VALIDAÇÃO
while True:
    try:
        peso = float(input('Peso (kg): '))
        altura = float(input('Altura (m) [ex: 1.75]: '))

        if peso > 0 and altura > 0:
            break
        else:
            print(f"{Fore.RED}ERRO: Peso e altura devem ser maiores que zero.")
    except ValueError:
        print(f"{Fore.RED}ENTRADA INVÁLIDA: Digite apenas números e use ponto para decimais.")

# 2. CÁLCULO DO IMC
# IMC = peso / (altura ** 2)
imc = peso / (altura ** 2)

print(f"\nO seu IMC é de {Fore.CYAN}{imc:.1f}")

# ------------------------------------------------------------------------------
# 3. LÓGICA DE STATUS (CUIDADO COM OS SINAIS!)
# ------------------------------------------------------------------------------
#

if imc < 18.5:
    print(f'Status: {Fore.YELLOW}ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print(f'Status: {Fore.GREEN}PESO IDEAL')
elif 25 <= imc < 30:
    print(f'Status: {Fore.YELLOW}SOBREPESO')
elif 30 <= imc < 40:
    print(f'Status: {Fore.RED}OBESIDADE')
else: # Caso seja 40 ou mais
    print(f'Status: {Fore.RED}{Style.BRIGHT}OBESIDADE MÓRBIDA')

print(f"{Fore.YELLOW}{'=' * 50}")