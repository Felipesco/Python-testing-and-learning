largura = float(input('Digite a Largura em metros: '))
altura = float(input('Digite a Altura em metros : '))

area = largura * altura 
tinta = area / 2
print('Essa parede de {} x {} tem uma área de {}m²'.format(largura, altura, area))
print('Você precisará de {}L para pintar essa parede'.format(tinta))

"""
Leia a largura
Leia a altura
calcule a área
calcule a quantidade de tinta (1Litro para 2m²)
"""
