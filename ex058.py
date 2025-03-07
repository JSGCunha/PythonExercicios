from random import randint
from time import sleep
tentativas = 0
computador = randint(0, 10)
jogador = int(input('Adivinhe em que número estou pensando entre 0 e 10: '))
while jogador != computador:
    jogador = int(input('Você errou! Tente novamente! Em que número estou pensando?  '))
    tentativas = tentativas + 1
    if jogador == computador:
        print('Parabens! Você acertou!')
print('Você acertou em {} tentativas!'.format(tentativas))