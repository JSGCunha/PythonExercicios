import random

vitorias_consecutivas = 0

while True:
    # Solicita ao jogador um número
    jogador = int(input("Escolha um número (0 a 10): "))

    # Solicita ao jogador se ele quer ser par ou ímpar
    escolha = input("Escolha Par ou Ímpar (P/I): ").strip().lower()

    # O computador escolhe um número aleatório
    computador = random.randint(0, 10)

    # Soma dos dois números
    soma = jogador + computador

    # Verifica se a soma é par ou ímpar
    if soma % 2 == 0:
        resultado = "par"
    else:
        resultado = "ímpar"

    # Verifica se a escolha do jogador está correta
    if (escolha == "p" and resultado == "par") or (escolha == "i" and resultado == "ímpar"):
        print(
            f"Você escolheu {jogador}, o computador escolheu {computador}. A soma deu {soma}, que é {resultado}. Você ganhou!")
        vitorias_consecutivas += 1
    else:
        print(
            f"Você escolheu {jogador}, o computador escolheu {computador}. A soma deu {soma}, que é {resultado}. Você perdeu!")
        break  # O jogador perdeu, então o jogo é interrompido

# Exibe o n
