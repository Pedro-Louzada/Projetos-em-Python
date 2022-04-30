print('=-'*5,'CONTADOR DE TERMOS EM PA','=-'*5)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10-1) * razão
for c in range(primeiro,décimo + razão,razão):
    print('{}'.format(c), end=' >')
print('ACABOU!')
