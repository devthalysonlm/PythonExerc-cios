#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de
# dias pelos quais ele foi alugado. Calucule o preço a pagar , sabendo que o carro custa R$60 por dia e R$ 0,15 por km rodado.

km = float(input('Digite a quantidade de km rodado:'))
dia = int(input('Digite a quantidade de dias percorridos:'))
prk = km * 0.15
prd = dia * 60
print('Foram {}km rodados , total a pagar: R${:.2f}\nForam {} dias utilizados , total a pagar R${:.2f}'.format(km, prk, dia, prd))







