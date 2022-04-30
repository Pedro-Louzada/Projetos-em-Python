print ('=-'*5, 'COTADOR DE PREÇO', '=-'*5)

prod = float(input('Qual é o valor do produto? '))
print('=-'*5,'FORMA DE PAGAMENTO','=-'*5)
resp = int(input('Digite 1 para À vista no dinheiro/cheque: \nDigite 2 para À vista no cartão: \nDigite 3 para parcelar até 2X no cartão: \nDigite 4 para parcelar em 3x ou mais:\n'))

if resp == 1:
    valorFinal = prod - (prod*0.1)
    print('O valor Final do produto foi de R${:.0f},00.'.format(valorFinal))
elif resp == 2:
    valorFinal = prod - (prod*0.05)
    print('O valor Final do produto foi de R${:.2f}.'.format(valorFinal))
elif resp == 3:
    valorFinal = prod
    print('O valor Final do produto foi de R${:.0f},00.'.format(valorFinal))
else:
    valorFinal = prod + (prod*0.2)
    print('O valor Final do produto foi de R${:.0f},00.'.format(valorFinal))