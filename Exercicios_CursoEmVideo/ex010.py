#Algoritmo: ler a quantidade de dinheiro e mostrar quantos dolares pode comprar, a cotação do dolar é de R$3,85
print('===== DESAFIO 10 =====')
real = float(input('Informe a quantidade de dinheiro: R$'))
dolar = real /3.71
coroaDin = real / 0.57
coroaNor = real / 0.45
euro = real / 4.26
print('Você possui R${:.2f}\nVocê pode comprar:\nDolar: US${:.2f}\nCoroa Dinamarquesa: Kr${:.2f}\nCoroa norueguesa: Kr{:.2f}\nEuro: £{:.2f}'.format(real, dolar, coroaDin, coroaNor, euro))
