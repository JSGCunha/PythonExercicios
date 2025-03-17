primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))

termo = primeiro
contador = 1
total_termos = 0
mais_termos = 10  # Começamos mostrando os 10 primeiros termos

while mais_termos != 0:
    total_termos += mais_termos
    while contador <= total_termos:
        print(termo, end=' → ')
        termo += razao
        contador += 1
    print('PAUSA')
    mais_termos = int(input('Quantos termos você quer mostrar a mais? (Digite 0 para parar): '))

print(f'Progressão finalizada com {total_termos} termos mostrados.')