maior = 0
nHomem = 0
nMulher = 0
while True:
    print('=-='*5)
    print('CADASTRO:')
    print('=-='*5)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if idade >= 18:
            maior += 1
        if sexo == 'M':
            nHomem += 1
        if sexo == 'F' and idade < 20:
            nMulher += 1
    resp = ' '
    while resp not in 'SN': #Enquanto a resp ñ estiver em S ou N...
        resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O número de pessoas maiores de idade foram de {maior}.')
print(f'O número de homens cadastrados foram de {nHomem}.')
print(f'O número de mulheres menores de idade foram de {nMulher}.')







