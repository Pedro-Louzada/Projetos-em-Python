from random import randint
from time import sleep #tempo entre as palavras serem exibidas
lista = {'Pedra','Papel','Tesoura'}
computador = randint(0,2)
print('Suas opções: \n[0] PEDRA\n[1] PAPEL\n[2] TESOURA')
usuario = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*11)
print('Computador jogou {}'.format(lista[computador]))
print('Jogador jogou {}'.format(lista[usuario]))
print('-='*11)
if computador == 0:
    if usuario == 0:
        print('EMPATE')
    elif usuario ==1:
        print('JOGADOR GANHOU')
    elif usuario == 2:
        print('COMPUTADOR GANHOU')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if usuario == 0:
        print('COMPUTADOR GANHOU')
    elif usuario == 1:
        print('EMPATE')
    elif usuario == 2:
        print('JOGADOR GANHOU')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if usuario == 0:
        print('JOGADOR GANHOU')
    elif usuario == 1:
        print('COMPUTADOR GANHOU')
    elif usuario == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')



