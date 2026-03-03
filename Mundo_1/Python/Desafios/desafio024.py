#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo"

print(f"{' Desafio 024 - Versão Final ':=^50}")
# 1. Entrada: Limpamos os espaços extras e já deixamos tudo em MAIÚSCULO
# Assim, se o usuário digitar 'santo', 'Santo' ou 'SANTO', o programa funciona!
cidade = str(input('digite o nome da sua cidade: ')).strip().upper()

#Logica# 2. Lógica:
# O .split() quebra o nome da cidade em uma lista de palavras.
# Ex: "Santo André" vira ["SANTO", "ANDRÉ"]
Palavra = cidade.split()

# Verificamos se a primeira palavra (índice 0) é "SANTO"
# O resultado será True (Verdadeiro) ou False (Falso)
resultado = Palavra[0] == 'SANTO'

#saida
print(f"Sua cidade começa com 'Santo'? {resultado} ")

# .upper() -> Normaliza o texto para que 'santo' e 'SANTO' sejam lidos da mesma forma.
# [:5] == 'SANTO' -> Fatiamos apenas as 5 primeiras letras para comparar com o alvo.
# O resultado é um tipo 'bool' (True ou False).