
nome = 'Lucas Souza'
altura = 1.90
peso = 90
imc = peso / (altura*altura)

# Lucas Souza tem 1.90 de altura
# pesa 84 quilos e seu IMC é

print (nome, 'tem', altura, 'de altura')
print ('pesa', peso, 'quilos e seu IMC é:')
print (f'{imc:.2f}')

print ()

if imc < 18:
    print ('Voce esta com Baixo Peso')
elif 18< imc <25:
    print('Voce esta com o Peso Normal')
else:
    print ('Voce precisa controlar o seu Peso - Possível Obesidade')