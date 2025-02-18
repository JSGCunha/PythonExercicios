import math
x= float(input('Digite o valor do ângulo a ser analisado: '))
sen = math.sin(x)
cos = math.cos(x)
tang = math.tan(x)
print(' O valor do Seno é {}, do Cosseno é {} e da Tangente é {}'.format(math.ceil(sen), math.ceil(cos), math.ceil(tang)))
