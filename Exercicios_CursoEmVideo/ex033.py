print('{} DESAFIO 33 {}'.format(('=' * 5), ('=' * 5)))
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))
menorN = n1
# Estrutura condicional para verificar o menor valor
if n2 < n1 and n2 < n3:
    menorN = n2
if n3 < n1 and n3 < n2:
    menorN = n3
# Estrutura condicional para verificar o maior valor
maiorN = n1
if n2 > n1 and n2 > n3:
    maiorN = n2
if n3 > n1 and n3 > n2:
    maiorN = n3
print('O maior valor foi {}\nO menor valor foi {}'.format(maiorN, menorN))
