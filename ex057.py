sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Digite na opção M ou F: ')).strip().upper()
print('Sexo registrado com sucesso!')
