from random import randint
itens = ('Pedra', 'Papel' , 'Tesoura')
computador = randint(0,2)
print('''Escolha uma opção:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual a sua jogada: '))
print('=*' * 15)
print('O jogador escolheu {}'.format(itens[jogador]))
print('O computador escolheu {}'.format(itens[computador]))
print('=*' * 15)
if computador == 0:
    if jogador == 0:
        print('Jogue novamente! Vocês escolheram PEDRA!')
    elif  jogador == 1:
        print('Você ganhou! PAPEL ganha de PEDRA')
    elif jogador == 2:
        print('O computador ganhou! PEDRA ganha de TESOURA')
elif computador == 1:
    if jogador == 1:
        print('Jogue novamente! Vocês escolheram PAPEL')
    elif jogador == 0:
        print('O computador ganhou! PAPEL ganha de PEDRA')
    elif jogador == 2:
        print('Você ganhou! TESOURA ganha de PAPEL')
elif computador ==2:
    if jogador == 2:
        print('Jogue novamente! Vocês escolheram TESOURA')
    elif jogador == 1:
        print('O computador ganhou! TESOURA ganha de PAPEL')
    elif jogador == 0:
        print('O computador ganhou! PEDRA ganha de TESOURA')
