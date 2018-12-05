from datetime import datetime
print('{} DESAFIO 41 {}'.format(('=' *5),('='*5)))
print('Nos dia 4 a a 5 de dezembro, ocorrerá o campeonato de natação')
print('Para concorrer participar da competição, basta escrever seu ano de nascimento que você será encaminhado para umas das categorias')
anoNascimento = int(input('Insira aqui o ano de seu nascimento: ')) 
anoAtual = datetime.today().year
idade = anoAtual - anoNascimento
if idade <= 9:
	categoria = 'MIRIM'
elif idade > 9 and idade <= 14:
	categoria = 'INFANTIL'
elif idade > 14 and idade < 20:
	categoria = 'JUNIOR'
elif idade == 20:
	categoria = 'SÊNIOR'
else:
	categoria = 'MASTER'
print('Sua idade é {} e estará participando na categoria {}'.format(idade,categoria))
