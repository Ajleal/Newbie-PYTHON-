nome = input ('Digite o nome do aluno ')
disc = input('Digite a disciplina ')
nota1 = int (input ('Digite a primeira nota ' ))
nota2 = int (input ('Digite a segunda nota '))
nota3 = int (input ('Digite a terceira nota '))
soma =  (nota1 + nota2 + nota3)
media = soma/3
if media ==10:
    print (nome,' CONGRATULATIONS *...*' , media, disc)
elif media <=6:
    print ('Estude mais um pouco ',media, disc)
else:
  print(nome, 'Aprovado, parabéns!!' ,media, disc)
