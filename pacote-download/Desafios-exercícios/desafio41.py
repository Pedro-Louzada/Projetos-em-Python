from datetime import date
atual = date.today().year

print('=-'*5, 'CATEGORIA DE ATLETAS', '=-'*5)

nascimento = int(input('DATA DE NASCIMENTO: '))
idade = atual - nascimento

print('O atleta tem {} anos.'.format(idade))

print('Processando ...')

if idade <= 9:
    print('Sua categoria é a MIRIM')
elif idade <= 14: # menor que 14 vai morrer no 9 pois tem um if que delimita isso em cima
    print('Sua categoria é a INFANTIL.')
elif idade <= 19:
    print('Sua categoria é a JUNIOR')
elif idade <= 25    :
    print('Sua categoria é a SêNIOR')
else:
    print('Sua categoria é a MASTER')
