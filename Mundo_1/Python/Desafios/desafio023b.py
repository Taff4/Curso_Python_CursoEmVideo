print(f"{' Desafio 023 (Versão String) ':=^50}")

# 1. Lemos como string e removemos espaços
# Não convertemos para int() aqui
num = input('Digite um número entre 0 e 9999: ').strip()

# 2. O SEGREDO: zfill(4)
# Se o usuário digitar '12', o zfill transforma em '0012'
# Isso garante que SEMPRE teremos os índices 0, 1, 2 e 3
num_formatado = num.zfill(4)

# 3. Saída usando os índices da string
# Lembre-se: em '1234', o milhar é o índice 0 e a unidade é o 3
print(f'Analisando o número {num}:')
print(f'Unidade: {num_formatado[3]}')
print(f'Dezena:  {num_formatado[2]}')
print(f'Centena: {num_formatado[1]}')
print(f'Milhar:  {num_formatado[0]}')

# u = n // 1 % 10 -> O operador // remove casas decimais e o % isola o último dígito.
# .zfill(4) -> (Se usar String) Garante que números curtos como '12' virem '0012'
# evitando o erro de "índice fora de alcance" (IndexError).