from math import hypot
print('{} DESAFIO 17 {}'.format(('='*5), ('='*5)))
catetoOposto = float(input('Informe o cateto Oposto: '))
catetoAdjacente = float(input('informe o cateto Adjacente: '))
print('Com os valores informados, a hipotenusa será {:.2f}'.format(hypot(catetoOposto, catetoAdjacente)))
