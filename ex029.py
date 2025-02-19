velocidade = float (input('Qual a velocidade está o seu carro? '))
if velocidade > 80:
    print('Você está acima da velocidade permitida de 80km/h')
    multa = (velocidade - 80) * 7
    print('o valor da sua multa é de {:.2f} reais'.format(multa))
else:
    print('Siga sua viagem e mantenha-se sempre abaixo dos limites de velocidade! ')
print('Boa viagem!')