soma_idade = 0
media_idade = 0
maior_idade_homem = 0
homem_mvelho = ' '
for c in range(1,5):
    nome = str(input('Digite o nome da pessoa {}: '.format(c))).strip().upper()
    idade = int(input('Digite o a idade da pessoa {}: '.format(c)))
    sexo = str(input('Digite o sexo (M/F) da pessoa {}:'.format(c))).strip().upper()
    soma_idade = soma_idade + idade
media_idade = soma_idade/4
print('A média de idade do grupo é de {} anos'.format(media_idade))





