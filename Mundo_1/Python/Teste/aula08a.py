# ==============================================================
# CURSO PYTHON #08 - UTILIZANDO MÓDULOS (GUSTAVO GUANABARA)
# ==============================================================
"""
DICA DE OURO: No PyCharm, se uma linha estiver cinza, é um aviso (warning).
Se estiver vermelha, é um erro. O aviso "Unused import" significa que você
importou algo mas ainda não usou no código.
"""

# 1. IMPORTAÇÕES (Sempre no topo do arquivo)
# -----------------------------------------------------------
# Aqui importamos apenas o que vamos usar para economizar memória.
from math import sqrt, floor, ceil

# 2. ENTRADA DE DADOS
# -----------------------------------------------------------
num = int(input('Digite um número: '))

# 3. PROCESSAMENTO
# -----------------------------------------------------------
raiz = sqrt(num)

# 4. SAÍDA DE DADOS (Diferentes formas de exibir)
# -----------------------------------------------------------
print('-' * 30)
print(f'RESULTADOS PARA O NÚMERO: {num}')
print('-' * 30)

# Exemplo 1: Raiz real com 2 casas decimais (f-string formatada)
print(f'Raiz real: {raiz:.2f}') 

# Exemplo 2: Arredondado para BAIXO (chão)
# Aqui usamos a função floor() que importamos lá no topo.
print(f'Arredondado para baixo (floor): {floor(raiz)}')

# Exemplo 3: Arredondado para CIMA (teto)
print(f'Arredondado para cima (ceil): {ceil(raiz)}')

# -----------------------------------------------------------
# EXPLICAÇÕES TÉCNICAS PARA ESTUDO:
# -----------------------------------------------------------
# [ import math ]      -> Traz a caixa toda. Usa-se math.sqrt()
# [ from math import ] -> Traz ferramentas soltas. Usa-se sqrt() direto.
# [ :.2f ]             -> Formata visualmente o número para 2 casas decimais.
# [ Unused Import ]    -> Aviso do PyCharm quando você importa e não usa a função.