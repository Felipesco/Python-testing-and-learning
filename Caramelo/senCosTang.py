# senCosTang.py == ex018.py
# Uso pessoal, me ajuda bastante
import math

angulo = float(input('Digite o angulo: '))

seno = math.sin(math.radians(angulo)) #converte o angulo para radiano e calcula o seu seno
cosseno = math.cos(math.radians(angulo)) #converte o angulo para radiano e calcula o seu cosseno
tangente = math.tan(math.radians(angulo)) #converte o angulo para radiano e calcula a sua tangente

print('O ângulo {} tem o seu SENO de {:.2f}'.format(angulo, seno))
print('O COSSENO é de {:.2f}'.format(cosseno))
print('A TANGENTE é de {:.2f}'.format(tangente))
