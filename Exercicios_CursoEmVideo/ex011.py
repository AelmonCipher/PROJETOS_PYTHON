#Algoritmo: ler largura e altura, calcular a area, mostrar a quantidade de tinta para pintar, sabe-se que cada litro de tinta pinta 2m(2)
print('===== DESAFIO 11 =====')
altura = float(input('Informe a altura da parede: '))
largura = float(input('Informe a largura da parede: '))
area = altura*largura
baldesTinta = area/2
print('Sua parede tem a dimensão de {}x{} e área de {}m²\n Será necessário {}l de tinta para pintar a parede'.format(altura, largura, area, baldesTinta))
