import sys
print('\33[7;30;m{} DESAFIO 44 {}\33[m'.format(('='*5),('='*5)))
precoProduto = float(input('Informe o Valor do Produto: '))
print('\33[7;30;mFormas de Pagamento Disponiveis\33[m')
print('A VISTA = 1\nCARTÃO = 2\n2X NO CARTÃO = 3\n3X OU MAIS NO CARTÃO = 4')
formaPagamento = int(input('Insira os números correspondentes a forma de pagamento: '))
if formaPagamento == 1:
    valorPago = precoProduto + ((precoProduto * 10) / 100)
elif formaPagamento == 2:
    valorPago = precoProduto + ((precoProduto * 5)/100)
elif formaPagamento == 3:
    valorPago = precoProduto
elif formaPagamento == 4:
    valorPago = precoProduto + ((precoProduto * 20) / 100)
else:
    print('\33[4;31;mERRO! Valor informado é inválido\33[m')
    sys.exit()
print('O valor a ser pago pelo produto será R$ {}'.format(valorPago))
