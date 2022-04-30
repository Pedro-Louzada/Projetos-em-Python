#1-fatiamento de strings
# exemplo : frase = CURSO EM VIDEO PYTHON
# os espaços entre as palavras também contam...
# frase[3] = S <- começa a contar do zero, ou seja, a letra C seria o número 0.
# frase [6:12] vai do espaçamento 6 ao 11
# o número depois dos dois pontos não conta...
#frase[6:12:2] número 2 representa que vai ser em passos de 2 em 2
#2-análise de strings
#len(frase)<- len vem de lenth ou seja comprimento da strigs
#nº de caracteres
#frase.count('o')<- programa vai contar quantas letras 'o' tem na string
#frase.count('o',0,13)<- do 0 ao 12 quantas letras o tem análise c/ fatiamento
#frase.find('deo')<- vai procurar no programa
# onde tem essa combinação de letras, ele vai indicar a posição
# onde começa esta combinação, que no caso, é na casa 11
#frase.replace("Python","Android") <- Ele irá reposicionar a palavra "Python" por "Android"
#frase.upper()<- transformará a frase toda em maiúscula
#frase.lower()<- transformará a frase toda em minúscula
#frase.capitalize()<- deixará somente a primeira letra em maiúsculo
#frase.title()<- dividirá as palavras, colocando a primeira letras de cada uma em maiúscula
#frase.strip()<- remove todos os espaços inúteis dentro da frase, do início e do final da frase
#frase.rstrip <- removerá os espaços a direita (RIGHT) e #frase.lstrip removerá os espaços a esquerda (LEFT)
#frase.split()<-divide uma frase em palavras únicas com individuais cadeias de caracteres