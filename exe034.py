'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250.00,calcule um aumento de 10%.
Para salaários inferiores  ou iguais, o aumento é de 15%.'''


from time import sleep

print('\033[1;36;40mVAMOS CALCULAR O SEU AUMENTO MEU CARO FUNCIONÁRIO!!!!!\033[m')
sal = float(input('Digite o valor do seu salário:R$'))
print('\033[35mCALCULANDO...\033[m')
sleep(3)
print('\033[35mCALCULANDO...\033[m')
sleep(3)
print('\033[35mCALCULANDO...\033[m')
sleep(3)
if sal > 1250:
    aumento = (sal * 10 / 100) + sal
    print('O seu salário anterior era de {}R${:.2f}{}. Com 10% de aumento vai para {}R${:.2f}{}'.format('\033[4;31m',sal,'\033[m','\033[4;32m',aumento,'\033[m'))
else:
    aumento = (sal * 15 / 100) + sal
    print('O seu salário anterior era de {}R${:.2f}{}. Com 15% e aumento vai para {}R${:.2f}{}'.format('\033[4;31m',sal,'\033[m','\033[4;32m',aumento,'\033[m'))









