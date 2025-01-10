import random

aluno = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))

alunos = [aluno, aluno2, aluno3, aluno4]

aleatorio = random.choice(alunos)

print('O aluno escolhido foi {}!'.format(aleatorio))
