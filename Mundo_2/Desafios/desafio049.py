"Refaça o desafio 9, mostrando a tabuada de um numero que o usuario escolher, só que agora utilizando um laço for."

from colorama import init, Fore

print(f"{Fore.CYAN}{'Desafio 49':=^50}")
print(f"{Fore.CYAN}{'REFATORANDO O DESAFIO 9':=^50}")

init(autoreset=True)

while True:
    try:
        n = int(input('Digite um número para ver sua tabuada: '))
        break
    except ValueError:
        print(f'{Fore.RED}ERRO.Digite um numero inteiro.')

print(f"{Fore.YELLOW}Tabuada de {n}:")
for i in range (1, 11):
        resultado = n * i
        print(f"{Fore.YELLOW}{n} x {i} = {resultado}")

print(f"\n{Fore.CYAN}{' FIM ':=^50}")







