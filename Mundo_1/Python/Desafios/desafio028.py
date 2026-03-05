from random import randint
from time import sleep # Faz o computador "esperar" alguns segundos

print(f"{' DESAFIO 028 ':=^50}")
print(f"{' JOGO DE ADIVINHAÇÃO ':=^50}")

# 1. O COMPUTADOR "PENSA" - sorteio
# randint(0, 5) sorteia um número inteiro entre 0 e 5 (incluindo o 5)
computador = randint(0, 5)

print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-' * 50)

# 2. ENTRADA DO JOGADOR
jogador = int(input('Em que número eu pensei? ')) #Tenta adivinhar

# 3. LOGICA COM SUSPENSE
print('PROCESSANDO...')
sleep(2) # Pausa o programa por 2 segundos para dar emoção

if jogador == computador:
    print(f'🎉 PARABÉNS! Você conseguiu me vencer! Eu pensei no {computador}.')
else:
    print(f'❌ GANHEI! Eu pensei no número {computador} e não no {jogador}!')

print(f"{' FIM ':^50}")