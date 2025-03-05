frase = str(input('Digite uma frase: ')) .upper().strip()
palavra = frase.split()
junto = ''.join(palavra)
print('Voce digitou a frase {}'.format(junto))
inverso = ''
for letra in range(len(junto) -1, -1, -1):
   inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')

