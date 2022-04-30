#crie um programa que leia o nome completo de uma pessoa e faça...
#nome em maiúsculo
#nome em minúsculo
#contar letras cem espaços
#quantas letras tem o primeiro nome
nome = str(input("Digite qual seu nome: ")).strip() #<-vai tirar todos os espaços entre as palvras
print("Analisando seu nome...")
print("Seu nome em maiúsculo é {}".format(nome.upper()))
print("Seu nome em minúsculo é {}".format(nome.lower()))
print("Seu nome tem {} caracteres.".format(len(nome)-nome.count(' ')))#contando com espaços...
#print("Seu 1º nome tem {} caracteres.".format(nome.find(' ')))
separa = nome.split()
print("Seu 1º nome tem {} caracteres.".format(len(separa[0])))