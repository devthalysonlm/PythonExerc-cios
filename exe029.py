'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada km acima do limite'''

from time import sleep
import emoji



print(': police_car_light:!!!RADAR REPORTADO A FRENTE!!!')

vel = float(input('Digite a velocidade do carro:'))
sleep(2)
print('ESCANEANDO VELOCIDADE, AGUARDE...')
sleep(2)
print('ESCANEANDO VELOCIDADE, AGUARDE...')
sleep(2)
print('ESCANEANDO VELOCIDADE, AGUARDE...')
sleep(2)
if vel > 80:
    multa = (vel - 80) * 7
    print('VOCÊ EXCEDEU O LIMITE DE VELOCIDADE')
    print('Sua multa será no valor de R${:.2f}'.format(multa))
else:
    print('Boa viagem')
    print('DIRIJA COM CUIDADO!!!')











