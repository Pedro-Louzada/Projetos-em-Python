num = qtd = soma = 0
while True:
    num = int(input('Digite qualquer valor [para parar digite 999]: '))
    if num == 999:
        break
    qtd += 1
    soma += num
print(f'Foram emitidos {qtd} números e a soma entre eles é {soma}.')
print('Até logo!')
