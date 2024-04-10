#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import  sin, cos, tan, radians
ângulo = float(input('Digite o ângulo que vc deseja:'))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('Seno:{:.2f}\nCosseno:{:.2f}\nTangente:{:.2f}'.format(seno, cosseno, tangente))










