'''Faça um programa que leia três números e mostre qual é o maior e qual é menor.'''

from time import sleep

print('\033[7;35;40mVAMOS BRINCAR DE MAIOR MENOR ????\033[m')
sleep(2)
a = int(input('\033[1;36mPrimeiro número:\033[m'))
b = int(input('\033[1;35mSegundo número:\033[m'))
c = int(input('\033[1;34mTerceiro número:\033[m'))
menor = a
if b < c and b < a:
    menor = b
if c < b and  c < a:
    menor = c
maior = a
if b > c and b > a:
    maior = b
if c > b and c > a:
    maior = c
    print('O maior número é {}{}{}'.format('\033[7;34;43m',maior,'\033[m'))
    print('O menor número é {}{}{}'.format('\033[7;33;44m',menor,'\033[m'))
else:
    print('Todos os números são iguais!!')































