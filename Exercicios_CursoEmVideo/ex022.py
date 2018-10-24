print('{} DESAFIO 22 {}'.format(('='*5), ('='*5)))
nome = str(input('Qual o seu nome completo? '))
primeiroNome = nome.split()
qtdLetrasPrimeiroNome = len(primeiroNome[0])
print('''O seu nome é {}
Nome com letras maiúsculas: {}
Nome com letras minúsculas: {}
Quantidade de letras desconsiderando os espaços: {}
Quantidade de letras no primeiro nome: {}'''.format(nome, nome.upper, nome.lower, (len(nome) - nome.find(' ')), qtdLetrasPrimeiroNome))
