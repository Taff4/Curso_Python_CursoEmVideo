# --- PARTE 1: INTERAÇÃO ---
# Use f-strings para injetar a variável direto no texto, fica mais elegante
nome = str(input('Qual é seu nome? ')).strip().title()

if nome == 'Rafael':
    print(f'Que nome lindo você tem, {nome}!')
else:
    print(f'Seu nome é tão comum, né, {nome}?')

print(f'Tenha um ótimo dia, {nome}!')
print('-' * 30) # Separador visual

# --- PARTE 2: NOTAS ---
# Dica: No PyCharm, coloque espaços entre operadores (n1 + n2) / 2
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

print(f'A sua média foi {media:.1f}')

# Condição Composta com um toque de "Emojis" para o console
if media >= 6.0:
    print('Sua média foi BOA! PARABÉNS! 🥳')
else:
    print('Sua média foi RUIM! Estude mais! 📚')

# --- PARTE 3: O PULO DO GATO (Simplificada) ---
# Em vez de apenas printar, você pode usar a simplificada para definir uma variável!
status = 'APROVADO' if media >= 6 else 'REPROVADO'
print(f'Resultado final: {status}')

print(f'{" FIM ":=^30}')

# --- EXEMPLO DE CONDIÇÃO COMPOSTA ---

velocidade = float(input('Qual é a velocidade atual do carro? '))

# O IF e o ELSE formam a estrutura composta
if velocidade > 80:
    print('⚠️  MULTADO! Você excedeu o limite permitido de 80km/h.')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
else:
    # Este bloco só executa se a velocidade for 80 ou menos
    print('✅ Dirija com segurança! Você está dentro do limite.')

print('--- Tenha um bom dia! ---')