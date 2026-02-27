print(f"{'Desafio 014' :=^50}")

#Escreva um programa que converta uma temperatura digitando em graus celsius e comverta graus para fahreint

#Entrada
c = float(input('Informe a temperatura em °C: '))

#calculo
F = c * 1.8 + 32
# F = ((9*C)/5)+32

#Saida
print('A temperatura de {:.1f}°C corresponde a {:.1f}°F'.format(c ,F))