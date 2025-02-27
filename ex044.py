preco = float(input('Digite o valor do produto: '))
print('''Selecione a forma de pagamento:
[1] À vista - DINHEIRO OU CHEQUE
[2] À vista - CARTÃO
[3] Em até 2X no CARTÃO
[4] 3X OU MAIS no CARTÃO''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    desconto = preco * 0.10
    valor_final = preco - desconto
    print('O valor do produto fica {} reais com 10% de desconto'.format(valor_final))
elif opcao == 2:
    desconto = preco * 0.05
    valor_final = preco - desconto
    print('O valor final do produto é {} com 5% de desconto'.format(valor_final))
elif opcao == 3:
    parcela = preco/2
    print('O valor do produto é {:.1f} reais e cada parcela fica no valor de {} reais.'.format(preco, parcela))
elif opcao == 4:
    desconto = preco + (preco * 0.20)
    parcela = desconto/4
    print('O valor do produto é {} com 20% de juros e cada parcela fica no valor de {} reais'.format(desconto, parcela))

