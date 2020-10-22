from math import trunc

numero = float(input('Digite um numero: '))

# Essas três linhas apresentam o mesmo resultado
#print('A parte inteira do numero {} ficará {}'.format(numero, trunc(numero)))
#print('A parte inteira do numero {} ficará {:.0f}'.format(numero, numero))
print('A parte inteira do numero {} ficará {}'.format(numero, int(numero)))
