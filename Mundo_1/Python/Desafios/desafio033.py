#Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor
print(f"{'Desafio 33':=^50}")

#entrada
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

#logica e condição
lista = [n1, n2, n2, n3]
menor = min(lista)
maior = max(lista)

#saida
print(f'O maior número foi {maior}')
print(f'O menor número foi {menor}')