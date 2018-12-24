player = object
nome = input ('digite seu nome: ')
idade = input ('digite sua idade ')
curso = input ('digite seu curso ')
disc = input ('digite as disciplinas cursadas ')
nota1 = int (input ('digite sua primeira nota: '))
nota2 = int (input ('digite sua segunda nota '))
soma = (nota1+nota2)
media = soma/2
dados = nome, idade, curso, disc, media
print ('O player 1 é', dados)
