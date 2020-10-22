#Aluguel de carros
dia = int(input('Por quantos dias o carro foi usado: '))
km = float(input('Andou quantos KM: '))

total = (dia * 60) + (km * 0.15)

print('O total a pagar será de R${:.2f}'.format(total))
