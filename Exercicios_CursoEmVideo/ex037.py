print('{} DESAFIO 37 {}'.format(('='*5), ('='*5)))
#entrada de dados
num = int(input('Informe um número para inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Qual a opção? '))
if opcao == 1:
    conversao = 'BINÁRIA'
    numConvert = bin(num)[2:]
elif opcao == 2:
    conversao = 'OCTAL'
    numConvert = oct(num)[2:]
elif opcao == 3:
    conversao = 'HEXADECIMAL'
    numConvert = hex(num)[2:]
else:
    print('Valor informado é inválido')
print('Conversão escolhida foi {}\nO número decimal digitado foi {}\nA conversão é igual a {}'.format(conversao, num, numConvert))
