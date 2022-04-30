lad1 = float(input('Informe o primeiro lado: '))
lad2 = float(input('Informe o segundo lado: '))
lad3 = float(input('Informe o terceiro lado: '))
if lad1 < lad2 + lad3 and lad2 < lad1 + lad3 and lad3 < lad1 + lad2:
    print("Os lados acima podem formar um triângulo ", end='')
    # pra depois que terminar ja cair o equilátero e nao pular linha usa-se essa funçaõ end
    if lad1 == lad2 == lad3:
        print('equilátero')
    elif lad1 != lad2 != lad3 != lad1:
        print('escaleno.')
    else:
        print('isóceles.')
else:
    print('Os lados acima não podem formar um triângulo')
