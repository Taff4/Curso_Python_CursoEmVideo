print(f"{'Desafio 007':=^50}")

#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua mèdia

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))

media = (n1 + n2) / 2

# Usando :.1f para a nota não ficar com muitas casas decimais
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, media))
