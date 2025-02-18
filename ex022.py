nome = input('Digite seu nome completo: ').strip()
print('Analisando seu nome...')
print('Em maiúsculo : {}'.format(nome.upper()))
print('Em minúsculo: {}'.format(nome.lower()))
print('Seu nome tema o todo {} letras'.format(len(nome)-nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e le tem {} letras'.format(separa[0], len(separa[0])))


