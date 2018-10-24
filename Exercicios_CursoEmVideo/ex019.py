from random import choice
print('{} DESAFIO 19 {}'.format(('='*5), ('='*5)))
aluno1 = str(input('Qual o nome do primeiro aluno? '))
aluno2 = str(input('Qual o nome do segundo aluno? '))
aluno3 = str(input('Qual o nome do terceiro aluno? '))
aluno4 = str(input('Qual o nome do quarto aluno? '))
print('O aluno sorteado para apagar o quadro foi {}'.format(choice([aluno1, aluno2, aluno3, aluno4])))