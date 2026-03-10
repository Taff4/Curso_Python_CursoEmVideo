from colorama import init, Fore

init(autoreset=True)
print(f"{Fore.CYAN}{' DESAFIO 052: DETECTOR DE PRIMOS ':=^50}")

while True:
    try:
        num = int(input("Digite um número: "))
        if num > 0:
            break
        print(f'{Fore.RED}Digite um número maior que zero.')
    except ValueError:
        print(f'{Fore.RED}ERRO! Digite um número inteiro válido.')

tot = 0  # Contador de divisores

# Vamos testar de 1 até o próprio número
for c in range(1, num + 1):
    if num % c == 0:
        print(f'{Fore.YELLOW}', end='') # Destaca os divisores em amarelo
        tot += 1
    else:
        print(f'{Fore.WHITE}', end='') # Números normais em branco
    print(f'{c} ', end='')

print(f'\n\nO número {num} foi divisível {tot} vezes.')

# REGRA DO PRIMO: Só pode ser dividido 2 vezes (por 1 e por ele mesmo)
if tot == 2:
    print(f'E por isso ele {Fore.GREEN}É PRIMO!')
else:
    print(f'E por isso ele {Fore.RED}NÃO É PRIMO!')

print(f"{Fore.CYAN}{'='*50}")