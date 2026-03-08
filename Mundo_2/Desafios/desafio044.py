"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento.
#Á VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO
#Á VISTA NO CARTÃO: 5% DE DESCONTO
#em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros
"""

from colorama import Fore, init

init(autoreset=True)

print(f"{Fore.CYAN}{' LOJAS LACERDA ':=^50}")

# 1. LOOP PRINCIPAL (Validação do Valor e Opção Inicial)
while True:
    try:
        valor_produto = float(input('Digite o valor do produto: R$ '))
        if valor_produto <= 0:
            print(f"{Fore.RED}ERRO: O valor deve ser maior que zero.")
            continue  # Volta para o início do loop

        print(f'''\nEscolha a forma de pagamento:
        [ 1 ] Dinheiro
        [ 2 ] Cartão
        [ 3 ] Pix''')
        escolha = int(input('Sua opção: '))

        if 1 <= escolha <= 3:
            break  # Sai do loop se o valor e a opção forem válidos
        else:
            print(f"{Fore.RED}OPÇÃO INVÁLIDA! Escolha 1, 2 ou 3.")

    except ValueError:
        print(f"{Fore.RED}ENTRADA INVÁLIDA: Digite apenas números.")

# ------------------------------------------------------------------------------
# 2. LÓGICA DE CÁLCULO
# ------------------------------------------------------------------------------

# --- OPÇÃO 1: DINHEIRO (10% de Desconto) ---
if escolha == 1:
    total = valor_produto - (valor_produto * 0.10)
    print(f"\nPagamento em {Fore.YELLOW}DINHEIRO{Fore.RESET}: 10% de desconto aplicado.")

# --- OPÇÃO 3: PIX (10% de Desconto) ---
elif escolha == 3:
    total = valor_produto - (valor_produto * 0.10)
    print(f"\nPagamento via {Fore.YELLOW}PIX{Fore.RESET}: 10% de desconto aplicado.")

# --- OPÇÃO 2: CARTÃO (Sub-menu de Parcelas) ---
elif escolha == 2:
    print(f'''\n{Fore.CYAN}--- OPÇÕES DO CARTÃO ---
    [ 1 ] À vista (5% de desconto)
    [ 2 ] 2x no cartão (Preço normal)
    [ 3 ] 3x ou mais (20% de juros)''')

    # Validação do sub-menu
    while True:
        try:
            parc_opcao = int(input('Qual a opção de parcelamento? '))
            if 1 <= parc_opcao <= 3:
                break
            print(f"{Fore.RED}Escolha uma opção de 1 a 3.")
        except ValueError:
            print(f"{Fore.RED}Digite um número inteiro.")

    # Lógica dentro do cartão
    if parc_opcao == 1:
        total = valor_produto - (valor_produto * 0.05)
        print("Pagamento à vista no cartão: 5% de desconto.")

    elif parc_opcao == 2:
        total = valor_produto
        print(f"Parcelado em 2x de R${total / 2:.2f} sem juros.")

    elif parc_opcao == 3:
        total = valor_produto + (valor_produto * 0.20)
        num_parcelas = int(input('Quantas parcelas? '))
        print(f"Parcelado em {num_parcelas}x de R${total / num_parcelas:.2f} com 20% de juros.")
else:
    print(f"{Fore.RED}ENTRADA INVÁLIDA")
# ------------------------------------------------------------------------------
# 3. RESULTADO FINAL
# ------------------------------------------------------------------------------
print(f"\nO produto de R${valor_produto:.2f} custará {Fore.GREEN}R${total:.2f}")
print(f"{Fore.CYAN}{'=' * 50}")