print('{} DESAFIO 30 {}'.format(('='*5), ('='*5)))
n = int(input('Informe um número: '))
d = n%2
if n == 0:
    print('{} é um número neutro'.format(n))
else:
    if d == 0:
        print('{} é um numero par'.format(n))
    else:
        print('{} é um número impar'.format(n))
