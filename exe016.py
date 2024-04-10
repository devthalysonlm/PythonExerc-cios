#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.
#EXE: Digite  um número: 6.127 >>> O número 6.127 tem a porção inteira 6.

from math import trunc
num = float(input('Digite um número:'))
print('O número digitado foi {} e sua parte inteira é {}'.format(num, trunc(num)))


# 2°Opção
'''num = float(input('Digite um valor:'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))'''
















