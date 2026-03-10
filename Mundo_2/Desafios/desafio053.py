"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços."
(Ex: "APOS A SOPA", "A SACADA DA CASA", "A TORRE DA DERROTA")
Voce pode ler de frente e pra tras é a mesma coisa.
"""

from colorama import init, Fore

init(autoreset=True)

print(f"{Fore.CYAN}{' DESAFIO 053: PALÍNDROMO ':=^50}")

while True:
    try:
        entrada = str(input('Digite uma frase: ')).strip().upper()
        if not entrada:
            print(f"{Fore.RED}Campo vazio!")
            continue

        # 1. REMOVER ESPAÇOS PARA JUNTAR TUDO
        # Ex: "APOS A SOPA" -> "APOSASOPA"
        junto = "".join(entrada.split())

        # 2. VALIDAÇÃO (Apenas letras)
        if not junto.isalpha():
            print(f"{Fore.RED}ERRO! Use apenas letras sem números ou símbolos.")
            continue
        break
    except Exception as e:
        print(f'{Fore.RED}ERRO: {e}')

# 3. GERANDO O INVERSO
inverso = ""
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(f"\nO inverso de {Fore.YELLOW}{junto}{Fore.RESET} é {Fore.YELLOW}{inverso}")

# 4. COMPARAÇÃO FINAL (FORA DO FOR!)
if inverso == junto:
    print(f"{Fore.GREEN}Temos um PALÍNDROMO!")
else:
    print(f"{Fore.RED}A frase digitada NÃO é um palíndromo.")

print(f"{Fore.CYAN}{'=' * 50}")

