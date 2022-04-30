#Faça um programa que calcule a Área da Parede
#e a qtd de Tinta para pinta-la (L de tinta pinta 2m²)

largura = float(input('Digite a largura de sua parede: '))
altura = float(input('Digite a altura de sua parede: '))
a = largura * altura
print ('A área de sua parede é: {}.'.format(a))
print('Você precisará de {} litros de tinta para pintar sua parede.'.format(a/2))