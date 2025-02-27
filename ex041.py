from datetime import datetime
ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

if idade <= 9:
    print('A categoria do atleta é MIRIM')
elif idade > 9 and idade <= 14:
    print('A categoria do atleta é INFANTIL')
elif idade > 14 and idade <= 19:
    print('A categoria do atleta é JUNIOR')
elif idade > 19 and idade <= 25:
    print('A categoria do atleta é SENIOR')
elif idade > 25:
    print('A categoria do atleta é master')


