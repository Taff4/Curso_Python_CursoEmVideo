#crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

print(f"{' Desafio 025 - Versão Final ':=^50}")
#Entrada
nome = str(input('Digite seu nome completo: ')).strip().upper()

# 2. Lógica (O Operador 'IN'):
# O 'in' verifica se a sequência de caracteres "SILVA" existe em qualquer lugar da string 'nome'.
# Ele já retorna True ou False automaticamente.
resultado = 'SILVA' in nome
#saida
print(f'Seu nome contem "Silva"? {resultado} ')

# 'SILVA' in nome -> O operador 'in' é a forma mais legível de verificar
# se um texto existe em qualquer parte da string (começo, meio ou fim).