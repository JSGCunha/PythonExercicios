# Lista para armazenar os números
numeros = []

# Lendo 50 números inseridos pelo usuário
tamanho = 50
for i in range(tamanho):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros += [numero]

# Local para armazenar números repetidos
repetidos = {}

# Verificando números repetidos
for i in range(len(numeros)):
    num = numeros[i]
    if num in repetidos:
        repetidos[num].append(i)
    else:
        repetidos[num] = [i]

# Exibindo números repetidos e suas posições
print("\nNúmeros repetidos e suas posições:")
for num, posicoes in repetidos.items():
    if len(posicoes) > 1:
        print(f"Número {num} encontrado nas posições: {', '.join(map(str, posicoes))}")
