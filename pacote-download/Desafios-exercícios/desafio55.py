maior = 0
menor = 0
for pessoas in range(1,6):
    peso = float(input('Peso da pessoa número {} : '.format(pessoas)))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {} quilos e o menor peso lido foi de {}'.format(maior, menor))
