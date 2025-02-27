altura = float(input('Qual a sua altura em cm: '))
peso = float(input('Qual o seu peso em Kg: ' ))
quadrado = altura**2
imc = peso/quadrado
print('Seu IMC é {:.2f}'.format(imc))

if imc <= 18.5:
    print('Classificação BAIXO PESO')
elif imc > 18.5 and imc <=25:
    print('Classificação PESO NORMAL')
elif imc >25 and imc <= 30:
    print('Classificação SOBREPESO')
elif imc > 30:
    print('Classificação OBESIDADE')
