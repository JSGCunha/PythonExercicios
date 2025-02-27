s1 = float(input('Digite o valor do primeiro segmento: '))
s2 = float(input('Digite o valor do segundo segmento: '))
s3 = float(input('Digite o valor do terceiro segmento: '))

if s1 < s2+s3 and s2 < s1+s3 and s3 < s1+s2:
    print('É possivel formar um triângulo com os seguimentos apresentados')
    if s1==s2==s3:
        print('Equilátero')
    elif s1 != s2 != s3 != s1:
        print('Escaleno')
    else:
        print('Isóceles')
