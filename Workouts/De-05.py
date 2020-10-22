# Um dado
import random 

numero = int(input('De 1 a 6, em qual número acha que o dado vai cair? '))

sorte = random.randint(1, 6)
print('O numero que caiu é....... {}!'.format(sorte))
if numero == sorte:
    print('Uau!! Você acertou!!')
else: 
    print('Que pena... Não foi dessa vez...')

