'''for c in range (1,10):
    print(c)
print('FIM!')'''
n= 1
par = 0
impar = 0
while n != 0:
    if n != 0:
        n = int(input('Digite um valor: '))
        if n % 2 == 0:
            par = par + 1

        if n % 2 != 0:
            impar = impar + 1
print('Foram digitados {} números pares'.format(par))
print('Foram digitados {} números ímpares'.format(impar))
print('FIM!')


