print('-'* 7 ,'PREÇO DA PASSAGEM', '-'* 7)

km = float(input('Informe a distância de sua viagem: '))

print('CALCULANDO O VALOR DE SUA PASSAGEM ...')

if km <= 200:
    valor = km * 0.5
    print('O valor da sua passagem é R${}.'.format(valor))
else:
    valor = km * 0.45
    print('O valor da sua passagem é R${}.'.format(valor))

