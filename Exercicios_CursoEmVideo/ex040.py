print('{} DESAFIO 40 {}'.format(('='*5),('='*5)))
nome = str(input('Informe o nome do aluno: ')) 
nota1 = float(input('Informe a nota da primeira avaliação: '))
nota2 = float(input('Informe a nota da segunda avaliação: '))
media = (nota1 + nota2) /2
if media >= 7:
	situacao = 'APROVADO'
elif media >= 5 and media < 7:
	situacao = 'RECUPERAÇÃO'
else:
	situacao = 'REPROVADO'
print('Nome : {}\nMédia: {}\nSituação: {}'.format(nome,media,situacao))
