real = float(input('Quanto dinheiro você tem? R$'))
dolar = real / 5.61
euro = real / 6.64

print('Com R${:.2f} você poderá comprar US${:.2f} ou €{}'.format(real, dolar, euro))
