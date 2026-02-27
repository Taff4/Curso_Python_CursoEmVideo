
#Faça um programa que leia um ãngulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ãngulo

# ==============================================================
# DESAFIO 018: TRIGONOMETRIA COM PYTHON
# ==============================================================

# Importamos as funções específicas da biblioteca 'math'.
# sin (seno), cos (cosseno), tan (tangente) e radians (conversor).
from math import radians, sin, cos, tan

# Criamos um cabeçalho centralizado com 50 caracteres para organização.
print(f"{' Desafio 018 ':=^50}")

# 1. ENTRADA DE DADOS
# Lemos o ângulo em graus (tipo float para aceitar decimais).
angulo = float(input("Digite o ângulo que você deseja: "))

# 2. CONVERSÃO ESSENCIAL
# O Python trabalha com RADIANOS por padrão em suas funções trigonométricas.
# Precisamos converter o ângulo de 'Graus' para 'Radianos' antes de prosseguir.
rad = radians(angulo)

# 3. PROCESSAMENTO (CÁLCULOS)
# Calculamos o seno, cosseno e tangente usando o valor já convertido em radianos.
seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)

# 4. EXIBIÇÃO DOS RESULTADOS
# Usamos f-strings para exibir os valores com apenas 2 casas decimais (:.2f).
print(f'\nPara o ângulo de {angulo}°:')
print(f'-> O SENO é {seno:.2f}')
print(f'-> O COSSENO é {cosseno:.2f}')
print(f'-> A TANGENTE é {tangente:.2f}')

# ==============================================================
# NOTA DE ESTUDO:
# Se você tentasse calcular sin(30) sem converter para radians,
# o resultado estaria errado porque o Python calcularia o seno
# de "30 radianos" (que é aprox. -0.98) em vez de "30 graus" (0.50).
# ==============================================================
