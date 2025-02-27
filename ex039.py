from datetime import datetime
ano_atual = datetime.now().year
ano_nascimento = int(input("digite seu ano de nascimento: "))
tempo = ano_atual - ano_nascimento
if tempo > 18:
    print('Você já deveria ter se alistado há {} anos!Você tem mais de 18 anos!'.format(tempo - 18))
elif tempo < 18:
    print('Você ainda não precisa se alistar!Espere {} anos!'.format(18 - tempo))
elif tempo == 18:
    print('Está na hora de se alistar! Você já tem 18 anos! ')

