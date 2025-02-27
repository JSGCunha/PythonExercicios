valor = float (input('Digite o valor do imóvel: '))
salario = float(input('Digite o valor do seu salário: '))
anos = int (input('Em quantos anos pretende pagar o imóvel: '))
qtdmeses = anos * 12
print('Você pretende pagar seu imóvel em {} meses'.format(qtdmeses))
parcelaimovel = valor/qtdmeses
print('O valor da sua parcela é de R${:.2f}'.format(parcelaimovel))
parcelamax = (salario * 30)/100

if parcelaimovel > parcelamax:
    print('Seu financiamento não foi aprovado pois a parcela excede 30% do seu salário!')
else:
    print('Seu financiamento foi aprovado. Parabéns!')
