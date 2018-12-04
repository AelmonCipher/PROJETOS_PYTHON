from datetime import datetime
print('{} DESAFIO 39 {}'.format(('=' *5),('='*5)))
anoNascimento = int(input('Informe o ano de nascimento: ')) 
anoAtual = datetime.today().year
idade = anoAtual - anoNascimento
if idade < 18:
	faltaAnos = 18 - idade
	print('Sua idade é {} anos'.format(idade))
	print('Você deverá se alistar daqui a {} anos'.format(faltaAnos)) 
elif idade == 18:
	print('Você tem {} anos de idade, está na hora de se alistar'.format(idade))
else:
	passouAnos = idade - 18
	print('Sua idade é {} anos'.format(idade))
	print('Você passou {} anos do tempo de alistamento'.format(passouAnos)) 
	
