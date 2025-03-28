while True:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número (maior que o primeiro): "))

    if num2 > num1:
        break  # Sai do loop se o segundo número for maior que o primeiro
    else:
        print("O segundo número deve ser maior que o primeiro. Tente novamente.")

soma = sum(range(num1, num2 + 1))
print("A soma dos números entre", num1, "e", num2, "é:", soma)