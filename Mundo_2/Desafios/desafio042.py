"""
Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostar que tipo de triângulo será formado:
#Equilatero: todos os lados iguais
#isoscels: dois lados iguais
#escaleno: todos os lados diferentes
"""

# ==============================================================================
#           DESAFIO 042: ANALISANDO TRIÂNGULOS v2.0
# ==============================================================================
from colorama import Fore, Style, init

init(autoreset=True)

print(f"{Fore.YELLOW}{' DESAFIO 42 ':=^50}")
print(f"{Fore.YELLOW}{' ANALISADOR DE TRIÂNGULOS ':=^50}")

# 1. ENTRADA COM VALIDAÇÃO
while True:
    try:
        r1 = float(input('Primeiro segmento: '))
        r2 = float(input('Segundo segmento: '))
        r3 = float(input('Terceiro segmento: '))
        if r1 > 0 and r2 > 0 and r3 > 0:  # Garante que não sejam valores nulos/negativos
            break
        print(f"{Fore.RED}ERRO: Os lados devem ser maiores que zero.")
    except ValueError:
        print(f"{Fore.RED}ENTRADA INVÁLIDA: Por favor, digite apenas números.")

# 2. LÓGICA PRINCIPAL (CONDIÇÃO DE EXISTÊNCIA)
if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print(f"\n{Fore.GREEN}Os segmentos acima PODEM FORMAR um triângulo ", end='')

    # 3. CLASSIFICAÇÃO ANINHADA (O QUE É NOVO)
    # Usamos o 'if' dentro do 'if' porque o tipo só existe se o triângulo existir.

    if r1 == r2 == r3:
        # Todos os lados iguais
        print(f"{Fore.CYAN}EQUILÁTERO!")

    elif r1 != r2 != r3 != r1:
        # Todos os lados diferentes
        # Dica: r1 != r2 != r3 não garante que r1 seja diferente de r3,
        # por isso adicionamos o != r1 no final para fechar o ciclo.
        print(f"{Fore.CYAN}ESCALENO!")

    else:
        # Se não é equilátero nem escaleno, sobrou apenas ser isósceles
        print(f"{Fore.CYAN}ISÓSCELES!")

else:
    print(f"\n{Fore.RED}Os segmentos acima NÃO PODEM FORMAR um triângulo.")

print(f"{Fore.YELLOW}{'=' * 50}")