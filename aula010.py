n1 = float (input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
m = (n1 + n2) / 2
print('A média das notas é {:.1f}'.format(m))
if m >= 6:
    print('Você foi aprovado')
else:
    print('Você foi reprovado')

