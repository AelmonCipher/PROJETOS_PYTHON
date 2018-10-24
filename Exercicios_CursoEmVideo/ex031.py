print('{} DESAFIO 31 {}'.format(('='*5), ('='*5)))
distancia = float(input('Qual a distância da viagem? '))
if distancia <= 200:
    precoPassagem = distancia * 0.50
else:
    precoPassagem = distancia * 0.45
print('A vaiagem será de {}km\nO valor da passagem será R${}'.format(distancia, precoPassagem))
print('Boa viagem')
