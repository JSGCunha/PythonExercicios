import random
import string

a = str (input('Digite o nome do primeiro aluno: '))
b = str (input('Digite o nome do segundo aluno: '))
c = str (input('Digite o nome do terceiro aluno: '))
d = str (input('Digite o nome do quarto aluno: '))
alunos = [a,b,c,d]
aluno_sorteado = random.choice(alunos)
print(' O aluno sorteado foi: {}'.format(aluno_sorteado))


