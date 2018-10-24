print('{} DESAFIO 34 {}'.format(('='*5), ('='*5)))
salario = float(input('Informe o salário: R$'))
if salario > 1250:
    novoSalario = ((salario*10)/100)+salario
else:
    novoSalario = ((salario * 15)/100)+salario
print('O salário era R${:.2f}, terá um aumento de 15%, o novo salário será R${:.2f}'.format(salario, novoSalario))
