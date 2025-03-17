# Inicializando as variáveis
contagem = 0
soma = 0

while True:
    # Lê o número digitado pelo usuário
    numero = int(input("Digite um número inteiro (999 para parar): "))

    # Condição de parada
    if numero == 999:
        break

    # Atualiza a soma e a contagem
    soma += numero
    contagem += 1

# Exibe o resultado final
print(f'Você digitou {contagem} números e a soma entre eles foi {soma}.')
