# Inicializando as variáveis
maior_18 = 0
homens = 0
mulheres_menor_20 = 0

while True:
    # Lê a idade e o sexo da pessoa
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M para masculino, F para feminino): ").strip().lower()

    # Verifica as condições para contagem
    if idade > 18:
        maior_18 += 1

    if sexo == 'm':
        homens += 1
    elif sexo == 'f' and idade < 20:
        mulheres_menor_20 += 1

    # Pergunta se o usuário quer continuar
    continuar = input("Deseja continuar? (S para sim, N para não): ").strip().lower()
    if continuar == 'n':
        break

# Exibe os resultados finais
print(f"A) Pessoas com mais de 18 anos: {maior_18}")
print(f"B) Quantidade de homens cadastrados: {homens}")
print(f"C) Mulheres com menos de 20 anos: {mulheres_menor_20}")
