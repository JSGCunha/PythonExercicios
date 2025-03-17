# Inicialização das variáveis
soma = 0
contador = 0

# Loop para ler os números
while True:
    numero = int(input("Digite um número inteiro (ou 999 para parar): "))

    # Verifica se o número é a condição de parada
    if numero == 999:
        break  # Sai do loop

    # Atualiza a soma e o contador
    soma += numero
    contador += 1

# Exibe o resultado
print(f"Quantidade de números digitados: {contador}")
print(f"Soma dos números digitados: {soma}")