#crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas.
#O nome com todas minusculas.
#Quantas letras ao todo(sem considerar espaços).
#Quantas letras tem o primeiro nome.


print(f"{'Desafio 022' :=^50}")

#Entrada:
# O .strip() já elimina espaços inúteis no início e fim
nome = str(input('Digite seu nome completo: ')).strip()

# Saída:
print(f'Nome em maiúsculas: {nome.upper()}')
print(f'Nome em minúsculas: {nome.lower()}')

# LÓGICA 1: Quantas letras ao todo (SEM espaços)
# Usamos o .replace(' ', '') para remover TODOS os espaços do meio do nome.
# Se o nome for "Ana Paula", o replace deixa "AnaPaula" (8 letras).
nome_sem_espacos = nome.replace(' ', '')
total_letras = len(nome_sem_espacos)

print(f'Seu nome tem ao todo {total_letras} letras.')

# 2. Quantas letras tem o primeiro nome:
# Lógica: O .split() transforma o nome em uma lista.
# O primeiro nome estará na posição [0]. Aí medimos o tamanho dele com len().
primeiro_nome = nome.split()[0]
print(f'Seu primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras.')

# .strip() -> Remove espaços inúteis que o usuário digita por erro.
# len(nome) - nome.count(' ') -> Cálculo matemático para ignorar espaços internos.
# nome.split()[0] -> A forma mais rápida de isolar a primeira palavra de uma lista.