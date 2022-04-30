#Crie um programa que calcule a hipotenusa de um triângulo
import math
compCatOposto = float(input('Informe o comprimento do cateto oposto: '))
compCatAdj = float(input('Informe o comprimento do cateto adjacente: '))
hip = math.pow(compCatOposto,2) + math.pow(compCatAdj,2)
print ('A hipotenusa desse triângulo é {}.'.format(math.floor(math.sqrt(hip))))