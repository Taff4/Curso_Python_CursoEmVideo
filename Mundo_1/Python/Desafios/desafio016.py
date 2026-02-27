print(f"{'Desafio016':=^50}")
# ==============================================================
# DESAFIO: PORÇÃO INTEIRA DE UM NÚMERO
# ==============================================================

# 1. IMPORTAÇÃO (A forma "Aula 08" de resolver)
from math import trunc

# 2. ENTRADA
num = float(input("Digite um número real: "))

# 3. SAÍDA (3 formas de fazer a mesma coisa)
# -----------------------------------------------------------

# Forma A: Usando o módulo MATH (Função trunc = Truncar/Cortar)
print(f"O número {num} tem a parte inteira {trunc(num)}")

# Forma B: Usando conversão de tipo (O jeito que você fez - perfeitamente válido!)
print(f"O número {num} tem a parte inteira {int(num)}")

# Forma C: Usando apenas formatação de string (Exibe sem decimais)
print(f"O número {num} tem a parte inteira {num:.0f}")

# -----------------------------------------------------------
# EXPLICAÇÃO PARA O SEU ESTUDO:
# -----------------------------------------------------------
# - int(num): Converte o valor para o tipo Inteiro.
# - math.trunc(): "Corta" o número na vírgula sem arredondar.
# - Diferença de FLOOR: O floor arredonda para baixo. Para números 
#   positivos é igual ao trunc, mas para negativos é diferente! 
#   Ex: floor(-3.5) vira -4, enquanto trunc(-3.5) vira -3.