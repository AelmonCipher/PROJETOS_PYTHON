from datetime import date
print('{} DESAFIO 32 {}'.format(('=' * 5), ('=' * 5)))
ano = int(input('Qual ano deseja analisar? Coloque 0 para o ano atual '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))
