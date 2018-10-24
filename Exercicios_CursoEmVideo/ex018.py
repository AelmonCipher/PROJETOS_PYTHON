from math import sin, cos, tan, radians
print('{} DESAFIO 18 {}'.format(('='*5), ('='*5)))
angulo = float(input('Informe um angulo para mostrar o seno, cosseno e tangente: '))
print('O angulo é {}\nO seno é {:.2f}\nO cosseno é {:.2f}\nA tagente é {:.2f}'.format(angulo, (sin(radians(angulo))), (cos(radians(angulo))), (tan(radians(angulo)))))
