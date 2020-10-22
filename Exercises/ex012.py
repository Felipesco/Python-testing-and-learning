valor = float(input('Digite o Preço do produto R$'))

desconto = valor - (valor * 5 /100)
print('O produto de R${:.2f}, você pagará somente R${:.2f}!!'.format(valor, desconto))
