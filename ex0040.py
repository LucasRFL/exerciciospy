prova = float(input('Qual foi a nota da sua prova: '))
trabalho = float(input('Qual foi a nota do seu trabalho: '))
media = (prova + trabalho) / 2

if media < 5:
    print('Tirando {} e {}, a média do aluno é {}'.format(prova, trabalho, media))
    print('O Aluno está em REPROVADO!')

elif media > 7:
    print('Tirando {} e {} a média do aluno é {}'.format(prova, trabalho, media))
    print('O Aluno está APROVADO!')

else:
    print('Tirando {} e {} a média do aluno é {}'.format(prova, trabalho, media))
    print('O Aluno está em RECUPERAÇÃO!')
