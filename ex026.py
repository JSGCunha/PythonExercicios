frase = str (input('Digite uma frase: ')).strip().upper()
print('O número de vezes que a letra A aparece na frase é {}'.format(frase.count('A')))
print('A letra A aparece a primeira vez na posição {}'.format(frase.find('A')+1))
print('A última posição da letra A é {}'.format(frase.rfind('A')+1))

