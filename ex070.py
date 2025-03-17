# Inicializando as variáveis
total_gasto = 0
produtos_acima_1000 = 0
produto_mais_barato = ''
preco_mais_barato = float('inf')  # Inicializa com um valor muito alto

while True:
    # Lê o nome e o preço do produto
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: R$"))

    # Atualiza o total gasto
    total_gasto += preco_produto

    # Verifica se o produto custa mais de R$1000
    if preco_produto > 1000:
        produtos_acima_1000 += 1

    # Verifica se o produto é o mais barato
    if preco_produto < preco_mais_barato:
        preco_mais_barato = preco_produto
        produto_mais_barato = nome_produto

    # Pergunta se o usuário quer continuar
    continuar = input("Deseja continuar? (S para sim, N para não): ").strip().lower()
    if continuar == 'n':
        break

# Exibe os resultados finais
print(f"\nA) Total gasto na compra: R${total_gasto:.2f}")
print(f"B) Quantidade de produtos que custam mais de R$1000: {produtos_acima_1000}")
print(f"C) Produto mais barato: {produto_mais_barato} (R${preco_mais_barato:.2f})")
