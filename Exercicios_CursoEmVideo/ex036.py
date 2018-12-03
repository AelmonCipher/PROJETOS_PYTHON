print('{} Desafio 36 {}'.format(('='*5),('='*5)))
#o usuário informa o valor da casa, o ssalário, os anos que ele irá pagar.
valorCasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu Salário? '))
qtdAnosPagar = float(input('Em quantos anos você irá pagar a casa? '))
#calcular a prestação mensal e minimo a pagar
prestacaoMensal = valorCasa/(qtdAnosPagar * 12)
minimo = (salario * 30)/100
#estrutura condicional para que caso a prestação seja maior que o minimo, o emprestimo seja negado
if prestacaoMensal <= minimo:
    concessao = 'CONCEDIDO'
else:
    concessao = 'NEGADO'
print('Emprestimo {}'.format(concessao))
