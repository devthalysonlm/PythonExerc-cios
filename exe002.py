'''Crie um script Python que leia o dia, mês e o ano de nascimento de uma pessoa e mostre uma mensage
com a data formatada'''

dia = int(input('Digite o dia de nascimento:'))
mes = str(input('Digite o mês de nascimento:'))
ano = int(input('Digite o ano de nascimento:'))
print('Você nasceu em {}/{}/{}'.format(dia, mes , ano))
