'''Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preoço da passsagem, cobrando R$0.50 por km para viagens até 200km e
0.45 para viagens mais longas.'''

print('\033[7;36;40mCACLCULANDO O PREÇO DAS PASSAGENS!!\033[m')
dst = float(input('Digite a disância da sua viagem:'))
if dst <= 200:
    preco = dst * 0.50
    print('A distância da viagem será de {}{}km{}. Preço total {}R${:.2f}{}'.format('\033[1;32m',dst,'\033[m','\033[1;31m',preco,'\033[m'))
else:
    preco = dst * 0.45
    print('A distãncia da viagem será de {}{}km{}. Preço total {}R${:.2f}{}'.format('\033[1;33m',dst,'\033[m','\033[1;34m',preco,'\033[m'))

















