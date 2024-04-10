#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.Faça um programa que ajude ...
#ele lendo o nome deles e escrevendo o nome do escolhido.

import random
a1 = input('Digite o nome do aluno:')
a2 = input('Digite o nome do aluno:')
a3 = input('Digite o nome do aluno:')
a4 = input('Digite o nome do aluno:')
lista = [a1, a2, a3, a4]
print('O aluno sorteado para apagar o quadro foi:{}'.format(random.choice(lista)))

