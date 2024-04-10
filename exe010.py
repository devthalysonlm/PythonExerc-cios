#Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar:
#Considerando U$ 1,00 = R$ 3,27

real = float(input('Digite quanto reais vc tem na carteira: R$ ' ))
dolar = real / 3.27
print('Com {:.2f} você pode comprar {:.2f} Dólares'.format(real, dolar))


