#Desenvolva um programa que pergunte a distancia em km.
#calcule o preço da passagem, cobrando 0,50 por km para viagens de até 200km e 0,45 para viagens mais longas

print(f"{' DESAFIO 031 ':=^50}")

# 1. Entrada
distancia = float(input('Qual a distância da sua viagem em Km? '))

# 2. Lógica e Condição
if distancia <= 200:
    preco = distancia * 0.50
else:
    # O else já entende que aqui a distância é MAIOR que 200
    preco = distancia * 0.45

#Outra maneira: simplificado
# preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

# 3. Saída Única
print(f'Sua viagem de {distancia}Km custará R${preco:.2f}')