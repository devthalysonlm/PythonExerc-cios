'''Faça um programa que leia o ano qualquer e mostre se ele é bissexto.'''

from datetime import date
print('\033[7;46;30mVAMOS CONCULTAR ANOS BISSEXTOS!!!\033[m')
ano = int(input('Digite o ano que quer consultar: Se por caso quiser saber o ano atual somente digite 0!'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[1;33m{} É BISSEXTO!!\033[m'.format(ano))
else:
    print('\033[1;34m{} NÃO É BISSEXTO!!\033[m'.format(ano))
















