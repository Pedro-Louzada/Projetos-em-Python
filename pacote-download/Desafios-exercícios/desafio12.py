#Faça um programa que leia o preço de um produto
#e mostre seu novo preço com 5% de desconto

preco = float(input('Qual preço avaliado por este produto R$ '))
print('O preço deste produto com 5% de desconto é: R${},00'.format(preco-(preco*0.05)))