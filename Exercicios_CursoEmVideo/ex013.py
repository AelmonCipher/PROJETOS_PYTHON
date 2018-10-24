print('===== DESAFIO 13 =====')
salario = float(input('Informe o salário: '))
novoSalario = salario+((15*salario)/100)
print('O salario era de R${:.2f}\nO aumeto é de 15%, o novo salário será R%{:.2f}'.format(salario, novoSalario))
