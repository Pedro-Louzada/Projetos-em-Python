print('=-'*5, 'Média Escolar', '=-'*5)

nota1 = float(input('Informe sua primeira nota: '))
nota2 = float(input('Informe sua segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('REPROVADO!')
elif media >=5 and media <= 6.9:
    print('RECUPERAÇÃO!')
elif media > 6.9:
    print('APROVADO!')