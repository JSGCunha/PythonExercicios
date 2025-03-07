from time import sleep

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
menu = -1
while menu != 0:
    menu = int(input('''Selecione a opção:
    [1] Somar
    [2] Subtrair
    [3] Multiplicar
    [4] Dividir
    [0] Finalizar
    Opção desejada: '''))
    if menu == 1:
        soma = n1 + n2
        print(' {} + {} = {}'.format(n1,n2,soma))
    if menu == 2:
        subtracao = n1 - n2
        print('{} - {} = {}'.format(n1, n2, subtracao))
    if menu == 3:
        multiplicacao = n1 * n2
        print('{} * {} = {}'.format(n1, n2, multiplicacao))
    if menu == 4:
        if n2 == 0:
            print('Erro: Divisão por zero!')
        else:
            divisao = n1 / n2
            print('{} / {} = {}'.format(n1, n2, divisao))
    if menu not in [0, 1, 2, 3, 4]:
        print('Opção inválida!')

print('Encerrando o programa...')
sleep(1)
print('Até logo!')


