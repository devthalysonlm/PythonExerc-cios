''' Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
exemplo: Digite um número: 1834 >>> unidade:4 dezena:3 centena:8 milhar:1'''

#Maneira matemática
num = int(input('Digite um número:'))
print('Unidade:{}'.format(num // 1 % 10))
print('Dezena:{}'.format(num // 10 % 10))
print('Centena:{}'.format(num // 100 % 10))
print('Milhar:{}'.format(num // 1000 % 10))


#Maneira String
'''num = int(input('Informe um número:'))
n =  str(num)
print('Unidade:{}'.format(n[3]))
print('Dezena:{}'.format(n[2]))
print('Centena:{}'.format(n[1]))
print('Milhar:{}'.format(n[0]))'''











