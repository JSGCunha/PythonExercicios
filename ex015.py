km = float(input('Quantos kilometros fora rodados com o carro: '))
dias = int(input('Quantos dias você alugou o carro: '))
diaria = 60*dias
consumo = km * 0.15
print('O valor a ser pago é {} \nsabendo que o valor total das diárias foram de R${} \ne do consumo de gasolina foi de R${}'.format(consumo+diaria, diaria, consumo))