#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = str(input('Digite um pruduto :'))
preco = float(input('Digite o preço do produto:R$'))
desc = preco - (preco * 5 / 100)
print('O preço do produto é {:.2f}, com 5% de desconto fica {:.2f}'.format(preco, desc))


