
n = int(input("Quantos termos da Sequência de Fibonacci você quer mostrar? "))

# Inicializa os dois primeiros termos da sequência
termo1 = 0
termo2 = 1

# Contador para controlar quantos termos já foram mostrados
contador = 0

# Loop para gerar e mostrar os termos da sequência
while contador < n:
    print(termo1, end=' → ')  # Mostra o termo atual
    proximo_termo = termo1 + termo2  # Calcula o próximo termo
    termo1 = termo2  # Atualiza o termo1 para o próximo cálculo
    termo2 = proximo_termo  # Atualiza o termo2 para o próximo cálculo
    contador += 1  # Incrementa o contador

print("FIM")  # Indica o fim da sequência