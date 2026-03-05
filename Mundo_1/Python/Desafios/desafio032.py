from calendar import isleap
from datetime import date

print(f"{' DESAFIO 032 ':=^50}")
ano = int(input('Digite o ano (coloque 0 para o ano atual): '))

# Se o usuário digitar 0, pegamos o ano atual do sistema
if ano == 0:
    ano = date.today().year
if isleap(ano):
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÃO É BISSEXTO!')