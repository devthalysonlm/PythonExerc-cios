#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o seu salário:R$'))
novo = salario + (salario * 15 / 100)
print('Seu salário de R${:.2f} vai para R${:.2f} com 15% de aumento'.format(salario, novo))


