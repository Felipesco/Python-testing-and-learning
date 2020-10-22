salario = float(input('Digite o salário R$'))
aumento = salario * 15 / 100 # + 15% em cima do salario
total = aumento + salario

print('Seu salário era de R${:.2f}, terá um aumento de {:.2f}'.format(salario, aumento))
print('Seu salário agora é de R${:.2f}'.format(total) )
