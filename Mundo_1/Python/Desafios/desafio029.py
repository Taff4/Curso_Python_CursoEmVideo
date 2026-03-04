#Escreva um programa que leia a velocidade de um corro
#Se ele ultrapassar a velocidade de 80km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar 7,00 por cada km acima do limite

print(f"{' DESAFIO 029 ':=^50}")

# 1. Entrada
velocidade = float(input('Qual é a velocidade atual do carro em Km/h? '))

# 2. Lógica e Condição
# Usamos uma Condição Composta para separar os dois caminhos
if velocidade <= 80:
    print(f'✅ Tenha um bom dia! {velocidade:.1f} Km/h está dentro do limite de 80 Km/h.')
else:
    # 3. Cálculo da Multa (Apenas se ele ultrapassar)
    # Subtraímos a velocidade do limite real (80)
    km_acima = velocidade - 80
    valor_multa = km_acima * 7.0

    print('⚠️  MULTADO! Você excedeu o limite de velocidade de 80 Km/h.')
    print(f'Você ultrapassou {km_acima:.1f} Km/h do limite permitido.')
    print(f'O valor da sua multa é de R${valor_multa:.2f}!')

print(f"{' FIM ':=^50}")