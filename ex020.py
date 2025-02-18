import random
import string

a = str (input('Digite o nome do primeiro aluno: '))
b = str (input('Digite o nome do segundo aluno: '))
c = str (input('Digite o nome do terceiro aluno: '))
d = str (input('Digite o nome do quarto aluno: '))
alunos = [a,b,c,d]
random.shuffle(alunos)
print('A odem das apresentações é :', alunos)
