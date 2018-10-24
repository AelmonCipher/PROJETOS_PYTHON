#Algoritmo: ler o preço de um produto e mostrar o valor com 5% de desconto
print('===== DESAFIO 12 =====')
precoP = float(input('Informe o preço do produto: R$'))
novoPreco = precoP-((5*precoP)/100)
print('O produto custava R${:.2f}\nCom a promoção de 5% de desconto, o novo preço será de R${:.2f}'.format(precoP, novoPreco))
