#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo...
#Calcule e mostre o comprimento da hipotenusa.

from math import hypot
cto = float(input('Digite o cumprimento do cateto oposto:'))
adj = float(input('Digite o cumprimento do cateto adjacente:'))
calculo = hypot(cto, adj)
print('O cumprimento da hipotenusa é {:.2f}'.format(calculo))


# 2°Opção

'''import math
cto = float(input('Digite o cumprimento do cateto oposto:'))
adj = float(input('Digite o cumprimento do cateto adjacente:'))
calculo = (cto ** 2) + (adj ** 2)
print('O cumprimento da hipotenusa é {:.2f}'.format(math.sqrt(calculo)))'''

# 3ºOpção
'''cto = float(input('Digite o cumprimento do cateto oposto:'))
adj = float(input('Digite o valor do cateto adjacente:'))
calculo = (cto ** 2 + adj ** 2) ** (1/2)
print('O valor da hipotenusa é {:.2f}'.format(calculo))'''




















