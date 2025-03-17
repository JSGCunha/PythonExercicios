# Inicialização das variáveis
soma = 0
contador = 0
maior = None
menor = None
continuar = 'S'

# Loop para ler os números
while continuar.upper() == 'S':
    numero = int(input("Digite um número inteiro: "))

    # Atualiza a soma e o contador
    soma += numero
    contador += 1

    # Atualiza o maior e o menor valor
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero

    # Pergunta ao usuário se deseja continuar
    continuar = input("Deseja continuar? (S/N): ").strip()

# Calcula a média
if contador > 0:
    media = soma / contador
else:
    media = 0

# Exibe os resultados
print(f"Média dos valores digitados: {media:.2f}")
print(f"Maior valor digitado: {maior}")
print(f"Menor valor digitado: {menor}")