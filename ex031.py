km = float(input('Digite o número de Kms que deseja percorrer em sua viagem: '))
if km <= 200:
    vpassagem = km * 0.5
    print(' O valor da sua passagem é {} Reais'.format(vpassagem))
else:
    v2passagem = km * 0.45
    print(' O Valor da sua passagem é {} Rais'.format(v2passagem))
print('Boa viagem!')
