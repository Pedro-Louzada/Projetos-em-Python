print('-'*6, 'PARADO!!', '-'*6)
print('Vamos verificar se ultrapassou nosso limite de velocidade ...')

velocidade = float(input('Informe qual a velocidade do seu veículo: '))

print('Processando ...')

if velocidade > 80:
    print('Você foi multado por ultrapassar os limites de velocidade!')
    multa = velocidade - 80
    valorMulta = 7 * multa
    print('Processando o valor da sua multa ...')
    print('O valor da sua multa foi de R${}.'.format(valorMulta))
else:
    print('Muito bem ..., você respeitou nosso limite de velocidade, pode seguir ...')