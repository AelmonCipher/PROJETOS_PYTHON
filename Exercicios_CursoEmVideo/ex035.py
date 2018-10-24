print('{} DESAFIO 35  {}'.format(('='*5), ('='*5)))
print('Informe três retas e eu irei calcular e mostrar se podem ou não formar um triângulo')
r1 = float(input('Informe a primeira reta: '))
r2 = float(input('Informe a segunda reta: '))
r3 = float(input('Informe a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com essas retas pode se formar um triângulo')
else:
    print('Não se pode formar um triangulo com essas retas')
