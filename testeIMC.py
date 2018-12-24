nome = input ('Digite seu nome: ')
idade = input ('Digite sua idade: ')
peso = float (input ('Digite seu peso: '))
alt = float (input ('Digite sua altura: '))
imc = peso / (alt*alt)
print ('Seu IMC é: {}'.format(imc))
if imc < 18.4:
    print ('precisa se alimentar ')
elif imc > 18.5 :
    print ('parabéns, regule-se ')
elif imc < 25 :
    print ('Saudavel')
elif imc > 26 :
    print ('sobre peso CUIDE-SE')
elif imc > 35 :
    print ('Obesidade nivel 1 ')
elif imc > 40 :
    print ('Obesidade nivel 2 ')
else :
    print ('OBESIDADE NIVEL 3, NECESSITA DE URGÊNCIA: ')
