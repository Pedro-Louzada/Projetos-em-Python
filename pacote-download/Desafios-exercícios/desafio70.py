from time import sleep
soma = maisMil = qtdP= menor = 0
barato = ''
while True:
    print('=-='* 8)
    print('CADASTRO DE PRODUTOS: ')
    print('=-=' * 8)
    prod = str(input('Produto: '))
    qtdP += 1
    preço = int(input('Preço: R$ '))
    if qtdP == 1:
        menor = preço
        barato = prod
    else:
        if preço < menor:
            menor = preço
            barato = prod
    soma += preço
    if preço > 1000:
        maisMil += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
sleep(0.3)
print(f'O total da compra foi R$ {soma:.2f}')
sleep(0.2)
print(f'Total de produtos que custam mais de 1.000 reais: {maisMil}')
sleep(0.2)
print(f'O produto mais barato custa R$ {menor:.2f}')
sleep(0.2)
print('{:-^40}'.format('FIM DO PROGRAMA'))


