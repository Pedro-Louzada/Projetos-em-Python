resp = ''
media = soma = qtd = 0
while resp != 'N':
    num = int(input('Informe algum número: '))
    soma += num
    qtd += 1
    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Deseja inserir mais valores? [S/N] ')).upper().strip()[0]
media = soma / qtd
print('A média dos valores foi de {:.2f}'.format(media))
print('O maior deles foi {} e o menor foi {}.'.format(maior,menor))