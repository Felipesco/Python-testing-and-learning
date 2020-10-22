celsius = float(input('Digite a temperatura em °C: '))

fahrenheit = ( (celsius * 9) / 5) + 32
print('A temperatura de {}°C é igual a {:.1f}°F.'.format(celsius, fahrenheit))

if celsius <= 12:
    print('QUE FRIOOOO!!!')
elif celsius <= 25:
    print('O clima tá bom')
else:
    print('TÁ QUENTE MAAISSS!!!')
