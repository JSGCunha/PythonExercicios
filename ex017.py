import math
#inserindo o valor dos catetos
x = float(input('Digite o comprimento do cateto oposto: '))
y = float(input('Digite o comprimento do cateto adjacente:   '))
hipotenusa = math.hypot(x,y)
print('O valor da Hipotenusa é {} '.format(math.ceil(hipotenusa)))
