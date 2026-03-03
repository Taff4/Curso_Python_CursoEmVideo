print(f"{' Praticando Manipulação de Strings ':=^50}")

# 1. ATRIBUIÇÃO E FATIAMENTO
frase = 'Curso em Vídeo Python'
# Pega do índice 3 ao 12 (o 13 é excluído)
print(f"Fatiamento [3:13]: {frase[3:13]}")

print('Oi')

# 2. TEXTOS LONGOS (Docstrings)
# Útil para menus, e-mails ou grandes blocos de explicação
texto_longo = """
Este é um exemplo de um texto muito longo.
Ele pode ter várias linhas, parágrafos,
e manter a formatação original.
"""
print(texto_longo)

# 3. MÉTODOS DE ANÁLISE (TUDO É OBJETO)
# Conta quantas vezes a letra 'o' aparece (minúscula)
print(f"Contagem de 'o': {frase.count('o')}")

# Encadeamento: Transforma em maiúsculo primeiro, depois conta os 'O'
print(f"Contagem de 'O' após .upper(): {frase.upper().count('O')}")

# len() mede o comprimento. .strip() remove espaços inúteis antes de medir
print(f"Tamanho sem espaços extras: {len(frase.strip())}")

# 4. TRANSFORMAÇÃO E IMUTABILIDADE
# replace() gera uma cópia com a troca, mas NÃO altera a variável original sozinha
print(f"Troca temporária: {frase.replace('Python', 'Android')}")

# Para alterar efetivamente, você deve SOBRESCREVER a variável:
frase = frase.replace('Python', 'Android')
print(f"Frase alterada permanentemente: {frase}")

# find() retorna a posição inicial. .lower() garante que encontre mesmo se estiver diferente
print(f"Posição de 'video' (em minúsculo): {frase.lower().find('video')}")

# 5. DIVISÃO E ACESSO A LISTAS
# .split() divide a frase pelos espaços e gera uma LISTA
dividido = frase.split()
print(f"Lista dividida: {dividido}")

# Acessando elementos da lista:
print(f"Primeira palavra da lista: {dividido[0]}") # Curso

# Acessando uma letra dentro de uma palavra da lista:
# Primeiro escolhemos a palavra [2] (Vídeo) e depois a letra [3] (e)
print(f"Quarta letra da terceira palavra: {dividido[2][3]}")