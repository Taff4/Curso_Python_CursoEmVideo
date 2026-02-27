from math import sqrt, hypot

print(f"{' Desafio 017 ':=^50}")

# Entrada
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))

# Opção A: Cálculo Manual (Pitágoras puro)
# hi = (co ** 2 + ca ** 2) ** (1/2) # Forma sem importar nada

# Opção B: Usando sqrt (Como você tentou fazer)
hi_manual = sqrt(co**2 + ca**2)

# Opção C: Usando a função própria para isso (Mais profissional)
hi_facil = hypot(co, ca)

# Saída
print(f'A hipotenusa vai medir {hi_facil:.2f}')

# -----------------------------------------------------------
# EXPLICAÇÃO PARA O SEU ESTUDO:
# -----------------------------------------------------------
# - hypot(co, ca): Esta função recebe os dois catetos e já faz
#   todo o cálculo de elevar ao quadrado, somar e tirar a raiz.
# - Erro comum: Somar as raízes dos catetos não resulta na
#   hipotenusa. É preciso somar os QUADRADOS deles.