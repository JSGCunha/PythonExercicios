from datetime import date
ano = int ( input('Que ano você quer analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))
