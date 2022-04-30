print('=-='*10)
print('Gerador de PA')
firstTerm = int(input('Primeiro termo: '))
reason = int(input('Razão: '))
cont = 1
termo = firstTerm
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += reason
        cont += 1
    print('PAUSA')
    mais = int(input('\nQuantos termos você quer mostrar a mais: '))
print('Progressão finalizafada com {} termos.'.format(total))








