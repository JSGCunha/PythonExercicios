n = str (input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
nome = n.split()
print(' primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

