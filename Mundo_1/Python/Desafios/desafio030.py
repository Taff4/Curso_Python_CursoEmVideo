#Crie um programa que leia um número inteiro e mostre se na tela se é par ou impar

print(f"{' DESAFIO 030 ':=^50}")

#entrada
numero = int(input('Digite um numero inteiro: '))

#logica e condição
if numero %2 == 0:
    print(f'O {numero} é par.')
else:
    print(f'O {numero} é ímpar.')

#Resultado da divisão 1 é impar
#resultado de 0 é par