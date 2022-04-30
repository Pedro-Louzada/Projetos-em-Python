#Crie um programa que pegue um valor em Reais($)
#e mostre quantos Dóllares(US$) está pessoa pode comprar

valor = float(input('Digite sua qtd de dinheiro em reais: '))
print('Você conseguirá comprar {}US$ dóllares.'.format(valor/3.27))