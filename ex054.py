from datetime import datetime
ano_atual = datetime.now().year
total_maior = 0
total_menor = 0
for nas in range(1,8):
    nasc = int(input('Digite o ano de nascimeto da pessoa {}: '.format(nas)))
    idade = ano_atual - nasc
    print('{} anos'.format(idade))
    if idade >=21:
        total_maior = total_maior + 1
    elif idade <= 20:
        total_menor = total_menor + 1
print('São {} maiores de idade e {} menores de idade'.format(total_maior, total_menor))


