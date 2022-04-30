num = int(input('Digite um núemro inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para binário é igual a {}'.format(bin(num)))
elif opção == 2:
    print('{} convertido para octal é igual a {}'.format(oct(num)))
elif opção == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(hex(num)))
else:
    print('OPÇÃO INVÁLIDA!')
