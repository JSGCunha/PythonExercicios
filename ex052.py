num = int(input('Digite um número: '))
total = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total = total + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[m O número {} foi divisível {} vezes.'.format(num, total))
if total == 2:
    print(' O {} é primo'. format(num))
else:
    print('o número {} não é primo'.format(num))



