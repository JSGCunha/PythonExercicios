r1 = float(input('Digite o tamanho da Reta 1: '))
r2 = float(input('Digite o tamanho da Reta 2: '))
r3 = float(input('Digite o tamanho da Reta 3: '))
if r1 < r2+r3 and r2 < r1+r3 or r3 < r1+r2:
    print('Esse é um triângulo retângulo')
else:
    print("Esse não é um triângulo retângulo")

