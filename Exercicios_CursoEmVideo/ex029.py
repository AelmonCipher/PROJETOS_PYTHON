print('{} DESAFIO 29 {}'.format(('='*5), ('='*5)))
velocidade = float(input('Qual a velociade do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi multado em R${}'.format(multa))
else:
    print('Parabéns, você está dentro do limite de velocidade.')
print('Dirija com segurança!')
