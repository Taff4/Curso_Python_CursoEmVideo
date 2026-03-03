#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra"A".
#Em que posição ela aparece a primeira vez
#em que posição ela aparece a ultima vez.


print(f"{'Desafio 026':=^50}")

# 1. Entrada: Limpamos espaços e padronizamos para maiúsculo
frase = str(input('Digite uma frase: ')).strip().upper()

# 2. Lógica:
# Quantas vezes aparece 'A'
quantidade = frase.count('A')

# Somamos +1 porque o Python começa no 0, mas para o usuário a 1ª posição é 1.
primeira_pos = frase.find('A') + 1

# Última ocorrência: .rfind() começa a procurar da DIREITA (fim) -> 'Right Find'
ultima_pos = frase.rfind('A') + 1
#saida
print(f'A letra "A" aparece {quantidade} vezes na frase.')
print(f'A primeira letra "A" apareceu na posição {primeira_pos}.')
print(f'A última letra "A" apareceu na posição {ultima_pos}.')

# .find('A') -> Procura a primeira ocorrência (da esquerda para a direita).
# .rfind('A') -> (Right Find) Procura a última ocorrência (da direita para a esquerda).
# + 1 -> Ajuste necessário porque o Python conta a partir do 0, mas humanos do 1.