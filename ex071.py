# Inicializa as cédulas disponíveis
cedulas = [50, 20, 10, 1]

while True:
    # Solicita o valor a ser sacado
    valor = int(input("Digite o valor a ser sacado (em R$): "))

    # Verifica se o valor é válido (não pode ser negativo ou zero)
    if valor <= 0:
        print("Valor inválido! Por favor, digite um valor positivo.")
        continue

    print(f"Valor a ser sacado: R${valor}")

    # Itera sobre cada tipo de cédula para calcular quantas serão entregues
    for cedula in cedulas:
        quantidade_cedulas = valor // cedula  # Calcula quantas cédulas dessa denominação
        if quantidade_cedulas > 0:
            print(f"Cédulas de R${cedula}: {quantidade_cedulas}")

        valor = valor % cedula  # Atualiza o valor com o restante após sacar as cédulas

    # Pergunta se o usuário deseja fazer outro saque
    continuar = input("\nDeseja realizar outro saque? (S para sim, N para não): ").strip().lower()
    if continuar == 'n':
        break
