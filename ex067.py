while True:
    # Solicita o número para mostrar a tabuada
    numero = int(input("Digite um número para ver a tabuada (número negativo para parar): "))

    # Condição de parada
    if numero < 0:
        break

    # Exibe a tabuada do número solicitado
    print(f'Tabuada do {numero}:')
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')

    print('-' * 20)  # Linha separadora para organizar a saída
