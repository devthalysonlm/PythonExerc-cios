#Crie um algoritimo e mostre o seu dobro, triplo e sua raiz quadrada.

from math import sqrt

num = int(input('Digite um número:'))
db = num * 2
ti = num * 3
rz = sqrt(num)
print('O número inforamdo foi {}\nSucessor: {}\nAntecessor: {}\nRaiz quadrada: {:.2f}'.format(num, db, ti, rz))




#Podemos fazer da seguinte maneira:

# n = int(input('Digite um número:'))
# d = n * 2
# t = n * 3
# r = n ** (1/2)
# print('De acordo com o valor informado \n'
#     'O dobro de {} é {} \n '
#     'O triplo de {} é {} \n '
#     'A raiz quadrada de {} é {:.2f}'.format(n, d, n, t, n, r))

#Podemos fazer da seguinte maneira:

# n = int(input('Digite um número:'))
# print('O dobro de {} vale {}'.format(n, (n * 2)))
# print('O triplo de {} vale {} e a raiz quadrada de {} vale {:.2f}'.format(n, (n * 3 ), n, pow(n, (1/2))))









