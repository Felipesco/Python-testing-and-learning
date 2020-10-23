# Medir a Hipotenusa de um Triângulo Retângulo
from math import hypot

print('Lembrando que essa conta é para um Triângulo Retângulo!')
co = float(input('Digite a medida do cateto Oposto: '))
ca = float(input('Digite a medida do cateto Adjasente: '))

hipotenusa = hypot(co, ca)
print('A hipotenusa é {:.2f}'.format(hipotenusa))
