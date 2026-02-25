print(f"{'Desafio 008':=^50}")

#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
metros = float(input('Digite o valor e metros: '))

cm = metros * 100
mm = metros * 1000
km = metros / 1000
hm = metros / 100
dam = metros / 10


# Usando o .format() que você prefere, mas com mais clareza:
print('A medida de {}m corresponde a:'.format(metros))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))
print('{:.0f}cm'.format(km))
print('{:.0f}mm'.format(hm))
print('{:.0f}cm'.format(dam))
