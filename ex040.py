n1 = float ( input('Digite a nota 1: '))
n2 = float (input('Digite a nota 2: '))
media = (n1 + n2) / 2
print('Sua média é {}'.format(media))

if media >= 7.0:
    print('Você foi aprovado!')
elif media < 6.9 and media >= 5.0 :
    print('Você está de recuperação!')
elif media < 5.0 :
    print('Você foi reprovado!')


