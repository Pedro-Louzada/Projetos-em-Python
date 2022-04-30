num = int(input('Digite um número para calcular seu fatorial: '))
cont = num
f = 1
print('Calculando {}! = '.format(num),end='')
while cont > 0:
    print('{}'.format(cont),end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1
print('{}'.format(f))
