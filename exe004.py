'''Faça um programa que leia  algo pelo teclado e mostre na tela o seu
tipo primitivo e todas as informações sobre ela :'''

algo = input('Digite qualquer coisa:')
print('Esse elemento é de que tipo ? {}'.format(type(algo)))
print('Esse elemento possui espaços? {}'.format(algo.isspace()))
print('É um elemento numérico? {}'.format(algo.isnumeric()))
print('É um elemento alfabético? {}'.format(algo.isalpha()))
print('Esta em em maúsculo ? {}'.format(algo.isupper()))
print('Esta em minúsculo ? {}'.format(algo.islower()))
print('É um elemento decimal ? {}'.format(algo.isdecimal()))
print('Este elemento esta captalizado ? {}'.format(algo.istitle()))
print('Esse elemento esta printável ? {}'.format(algo.isprintable()))
print('Esse elemento é identificável ? {}'.format(algo.isidentifier()))
print('Esse elemento consta na tabela ASCII ? {}'.format(algo.isascii()))
print('Esse elemento foi digitado ? {}'.format(algo.isdigit()))
print('Esse elemento é alphanumérico ? {}'.format(algo.isalnum()))

















