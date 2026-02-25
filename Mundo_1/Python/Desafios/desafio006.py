print(f"{' Desafio 006 ':=^50}")

#Crie um algoritmo que leia um número e mostre o seu dobro triplo e raiz quadrada
n = int(input('Digite um número: '))

# Cálculos corrigidos
d = n * 2
t = n * 3
r = n ** (1/2) # Ou n ** 0.5

print('O número {} tem o dobro {}, seu triplo é {} e a raiz quadrada é {:.2f}.'.format(n, d, t, r))