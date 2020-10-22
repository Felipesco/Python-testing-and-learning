#sorteio
import random

nome1 = str(input('1° pessoa, digite seu nome: '))
nome2 = str(input('2° pessoa, digite seu nome: '))
nome3 = str(input('3° pessoa, digite seu nome: '))
nome4 = str(input('4° pessoa, digite seu nome: '))

lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)

print('A pessoa escolhida foi: {}'.format(escolhido))
