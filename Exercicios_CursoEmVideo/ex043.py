print('{} DESAFIO 43 {}'.format(('='*5),('='*5)))
peso = float(input('Informe o seu peso em quilos: '))
altura = float(input('Informe sua altura em metros: '))
imc = peso/altura**2
if imc <= 18.5:
    result = str('abaixo do peso')
elif imc > 18.5 and imc < 25:
    result = str('com peso ideal')
elif imc >= 25 and imc <= 30:
    result = str('com sobrepeso')
elif imc > 30 and imc <= 40:
    result = str('com obesidade')
else:
    result = str('com obesidade mórbida')
print('Seu IMC é igual a {}, você está {}'.format(imc, result))
