# Faça um programa que leia a largura e a altura  de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessãria para pintá-la, sabendo que cada litro de tinta, pinta um área de 2m².

larg = float(input('Digite a largura da parede:'))
alt = float(input('Digite a altura de parede:'))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede será necesário {}l de tinta'.format(tinta))


