'''Faça um programa que leia o nome completo de uma pessoa , mostrando em seguida o primeiro e o
último nome separdamente. Exe: Ana Maria de Souza >> primeiro: Ana Último: Souza'''


name = str(input('Digite seu nome completo:')).strip()
n = name.split()
print('O seu primeiro nome é {}'.format(n[0]))
print('O seu segundo nome é {}'.format(n[-1]))































