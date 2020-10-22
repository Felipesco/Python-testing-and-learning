# Sorteio em lista
from random import shuffle

n1 = str(input('1° pessoa: '))
n2 = str(input('2° pessoa: '))
n3 = str(input('3° pessoa: '))
n4 = str(input('4° pessoa: '))

lista = [n1, n2, n3, n4]
shuffle(lista)

print('A ordem é: ')
print(lista)