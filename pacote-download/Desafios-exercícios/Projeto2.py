from random import randint

programa = randint(0,50)

print('Tente adivinhar um número sorteado de 0 a 50 ...')

usu = int(input('Digite qual número você escolheu: '))

if usu > programa:
    print('Chute um valor mais baixo ...')
elif usu < programa:
    print('Chute um valor mais alto ...')
else:
    print('Parabéns, você acertou. É uma pessoa de sorte!')