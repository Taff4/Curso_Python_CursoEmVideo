from colorama import Fore, init

init(autoreset=True)

print(f"{Fore.CYAN}{' DESAFIO 048 ':=^50}")

# 1. Inicializamos as variáveis de controle fora do laço
soma = 0  # ACUMULADOR (vai somar os valores: 3 + 9 + 15...)
cont = 0  # CONTADOR (vai contar: 1, 2, 3...)

# 2. Otimização: range(1, 501, 2) já pega apenas os ímpares
for c in range(1, 501, 2):
    # Se o número for múltiplo de 3
    if c % 3 == 0:
        cont += 1      # Encontrei um número, somo +1 ao contador
        soma += c      # Pego o valor de c e acumulo na variável soma

# 3. Saída formatada
print(f"A soma de todos os {Fore.YELLOW}{cont}{Fore.RESET} valores solicitados é {Fore.GREEN}{soma}")

print(f"\n{Fore.CYAN}{' FIM ':=^50}")