genre = str((input('Informe seu sexo: [M/F]: '))).strip().upper()[0]
while genre not in "MmFf":
    genre = str(input(print('Dados inválidos! Por favor informe seu sexo: '))).strip().upper()[0]
print('Sexo {} cadastrado com sucesso!'.format(genre))
