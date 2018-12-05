import sys
from random import choice
print('\33[7;4;30m {} DESAFIO 45 {}\33[m'.format(('='*5),('='*5)))
print('Vamos brincar de Jokenpô?')
usuario = str(input('Escreva pedra, papel ou tesoura: '))
computador = choice(['PEDRA', 'PAPEL', 'TESOURA'])
if usuario.upper() == computador:
    status = 'Empatamos'
elif (usuario.upper() == 'PEDRA' and computador == 'TESOURA') or (usuario.upper() == 'TESOURA' and computador == 'PAPEL') or (usuario.upper() == 'PAPEL' and computador == 'PEDRA'):
    status = 'Parabéns você ganhou'
elif (usuario.upper() == 'PEDRA' and computador == 'PAPEL') or (usuario.upper() == 'TESOURA' and computador == 'PEDRA') or (usuario.upper() == 'PAPEL' and computador == 'TESOURA'):
    status = 'Que pena eu venci'
else:
    print('\33[4;31mErro! você informou um jogada inválida\33[m')
    sys.exit()
print('Você jogou {}\nEu jogo {}\n{}'.format(usuario.upper(), computador, status))
