from random import randint
from time import sleep
print('{} DESAFIO 28 {}'.format(('='*5), ('='*5)))
comp = randint(0,5)
print('-=-'*20)
print('Vou pensar em um número de 0 a 5, tente adivinhar...')
print('-=-'*20)
sleep(3)
usuario = int(input('Em que número eu pensei '))
print('PROCESSANDO...')
sleep(3)
if comp == usuario:
    print('parabéns, você acertou, eu tinha pensado no número {}'.format(comp))
else:
    print('eu ganhei, eu pensei no número {} e você disse o número {}'.format(comp, usuario))
