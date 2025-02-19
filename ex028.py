from random import randint
from time import sleep

computador = randint(0, 5)
jogador = int(input('Adivinhe em que número estou pensando entre 0 e 5: '))
print('Processando...')
sleep((3))
if jogador == computador:
    print('Você acertou! Parabens!')
else:
    print('Errado! eu pensei no {} e não no {} '. format(computador, jogador))