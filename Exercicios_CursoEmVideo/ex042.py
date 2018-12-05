print('{} DESAFIO 42  {}'.format(('='*5), ('='*5)))
print('Informe três retas e eu irei calcular e mostrar se podem ou não formar um triângulo')
r1 = float(input('Informe a primeira reta: '))
r2 = float(input('Informe a segunda reta: '))
r3 = float(input('Informe a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    podeTriangulo = 'Com essas retas pode se formar um triângulo'
    if r1 == r2 and r2 == r3:
        tipoTriangulo = 'Equilatero'
    elif r1 == r2 or r1 == r3 or r2 == r3:
        tipoTriangulo = 'Isorceles'
    elif r1 != r2 and r1 != r3 and r2 != r3:
        tipoTriangulo = 'Escaleno'
else:
    podeTriangulo = 'Não se pode formar um triangulo com essas retas'
    tipoTriangulo = 'Inexistente'
print('Pode formar Trinagulo: {}\nTipo de triangulo: {}'.format(podeTriangulo, tipoTriangulo))
