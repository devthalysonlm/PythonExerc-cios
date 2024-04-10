'''Desenvolva um programa que leia o cumprimento de três retas e diga ao usuário se elas podem ou não
formar um triângulo..'''


print('\033[7;33mBRINCANDO COM AS RETAS...\033[m')
r1 = float(input('\033[32mPrimeiro segmento:\033[m'))
r2 = float(input('\033[31mSegundo segmento:\033[m'))
r3 = float(input('\033[34mTerceiro segmento:\033[m'))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('\033[32mÉ possível formar um trinângulo com esses segmentos!\033[m')
else:
    print('\033[31mNão é possível formar um triângulo com esses segmentos!\033[m')











