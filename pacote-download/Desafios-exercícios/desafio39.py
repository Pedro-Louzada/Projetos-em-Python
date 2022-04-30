print('=-'*5, 'Registro de Alistamento Militar', '=-'*5)

age = int(input('Informe sua idade: '))

if age == 18:
    print('Parabéns, chegou sua hora de se alistar!')
elif age > 18:
    tempex = age - 18
    print('Preste Atenção! Ja excedeu o tempo do seu alistamento em {} anos!'.format(tempex))
else:
    temprest = 18 - age
    print('Ainda não chegou sua hora de se alistar! Faltam {} anos.'.format(temprest))