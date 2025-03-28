#lista de notas
notas = [73, 67, 38, 33]
resultado = []

print("Processo de arredondamento de notas:")
print("-----------------------------------")

#demosntração dos arredondamentos
for nota in notas:
    print(f"\nNota original: {nota}")
#caso em que as notas são inferiores a 38
    if nota < 38:
        print("Nota abaixo de 38 - mantida nota original")
        resultado.append(nota)
    else: #caso em que diferença entre uma nota e o próximo número múltiplo de 5
        multiplo = ((nota // 5) + 1) * 5
        diferenca = multiplo - nota
        print(f"Próximo múltiplo de 5: {multiplo}")
        print(f"Diferença: {diferenca}")
          #quando o múltiplo for menor que 3
        if diferenca < 3:
            print(f"Arredondando para {multiplo}")
            resultado.append(multiplo)
        else:
            print("Diferença de 3 ou mais - mantida nota original")
            resultado.append(nota)
#resultado final das notas
print("\nNotas finais:")
print("---------------")
print(', '.join(map(str, resultado)))