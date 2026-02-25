print(f"{'Desafio 011' :=^50}")

#Faça um programa que leia a largura e a altura de uma parede em metros
#calcule a sua area e a quantidade de tinta necessaria para pinta-la
#sabemos qe cada litro de tinta, pinta uma área de 2m2.

# Entrada
largura = float(input('Largura da parede (m): '))
altura = float(input('Altura da parede (m): '))

# Cálculo da Área
area = largura * altura

# Cálculo da Tinta (Área dividida pelo rendimento de 2m² por litro)
tinta = area / 2

# Saída
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {:.2f}L de tinta.'.format(tinta))

