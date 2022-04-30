#Crie um programa que calcule o sen, cos e tg de um ângulo qualquer
import math
angulo = int(input('Digite qualquer ângulo: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print ('O seno de {} é {:.2f}.'.format(angulo,seno))
print ('O seno de {} é {:.2f}.'.format(angulo,cos))
print ('O seno de {} é {:.2f}.'.format(angulo,tan))