#lista de temperaturas
temperaturas = [23.6, 37.9, 25.1, 19.0, 29.8]

menor_temp = temperaturas[0]
maior_temp = temperaturas[0]
soma_temp = 0

print("As temperaturas informadas foram:", " ".join(map(str, temperaturas)))
#percorrendo a lista para encontrar maior, menor  valor e calcular soma dos valores
tamanho = len(temperaturas)
for temp in temperaturas:
    if temp < menor_temp:
        menor_temp = temp
    if temp > maior_temp:
        maior_temp = temp
    soma_temp += temp
#cálculo da média das temperaturas
media_temp = soma_temp / tamanho

# Exibição de resultados
print("A menor temperatura é:", menor_temp)
print("A maior temperatura é:", maior_temp)
print("A temperatura média é: {:.2f}".format(media_temp))