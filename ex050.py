soma = 0
cont = 0
for c in range (1,7):
  n = int(input('Digite um número: '))
  if n % 2 == 0:
      soma = n + c
      cont = n +1
print('Você informou {} númeoros pares e a soma é {}'.format(cont,soma))