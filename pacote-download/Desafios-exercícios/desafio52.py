num = int(input('Digite um valor: '))
tot = 0
for c in range(1,  num+1):
    if num % c == 0:
        print("\033[34m", end=' ')
        tot += 1
    else:
        print('\033[m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('\n\033[mE por isso ele é um número primo!')
else:
    print('E por isso ele não é um número primo!')