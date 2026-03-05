#Desenvolva um programa que leia o comprimeto de tres retas e diga ao usuario se elas podem ou não formar um triangulo
print(f"{'Desafio 35':=^50}")

#entrada
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
#logica
# Verifica a condição de existência de um triângulo
if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print("As retas podem formar um triângulo.")
    # Classificação adicional (opcional)
    if r1 == r2 == r3:
        print("Tipo: Equilátero")
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print("Tipo: Escaleno")
    else:
        print("Tipo: Isósceles")
else:
    print("As retas não podem formar um triângulo.")