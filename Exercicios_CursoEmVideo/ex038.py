print('{} DESAFIO 38 {}'.format(('='*5),('='*5)))
n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe O segundo valor: '))
if n1 > n2:
    print('O primeiro valor é maior')
elif n1 < n2:
    print('O Segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')
