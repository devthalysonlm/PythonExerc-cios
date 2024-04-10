'''Escreva um programa que faça o computador ''pensar'' em um número inteiro entre 0 e 5 e peça para
o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela
se o usuário venceu ou perdeu.'''


import random
from time import sleep

num = random.randint(0, 5) #Faz o computador 'PENSAR'
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar ...')
print('-=-' * 20)
user = int(input('Qual número eu escolhi?'))  #Pede para o jogador advinhar
print('PRCESSANDO...')
sleep(2)
if user == num:
    print('O número que eu escolhi foi {}, PRABÉNS!'.format(num))
else:
    print('O número que eu escolhi foi {}, o computador venceu!'.format(num))






















