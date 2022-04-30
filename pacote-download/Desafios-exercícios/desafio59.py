from time import sleep
value1 = int(input('Primeiro valor: '))
value2 = int(input('Segundo valor: '))
sleep(1)
option = 0
while option != 5:
    sleep(1)
    print('''    [1] SOMA
    [2] MULTIPLICAÇÃO
    [3] MAIOR
    [4] NOVOS NÚMEROS 
    [5] SAIR DO PROGRAMA''')
    sleep(1)
    option = int(input('Qual será sua opção: '))
    if option == 1:
        soma = value1 + value2
        sleep(1)
        print('A soma entre {} e {} é {}.'.format(value1,value2,soma))
        sleep(1)
    elif option == 2:
        produto = value1 * value2
        sleep(1)
        print('A multiplicação entre {} e {} é {}.'.format(value1,value2,produto))
        sleep(1)
    elif option == 3:
        if value1 > value2:
            maior = value1
        else:
            maior = value2
        sleep(1)
        print('O maior entre {} e {} é {}.'.format(value1,value2,maior))
        sleep(1)
    elif option == 4:
        sleep(1)
        print('Informe os números novamente: ')
        sleep(1)
        n1 = int(input('Primeiro valor: '))
        sleep(1)
        n2 = int(input('Segundo valor: '))
    elif option == 5:
        sleep(1)
        print('Finalizando...')
        sleep(1)
    else:
        sleep(1)
        print('Opção inválida, tente novamente!')
        sleep(1)
    print('=-='*10)
sleep(1)
print('Fim do programa, volte sempre! ')


