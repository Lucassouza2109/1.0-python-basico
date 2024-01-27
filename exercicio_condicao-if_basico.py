primeiro_valor = input ('Digite um valor: ')
segundo_valor = input ('Digite um valor: ')

condicao1 = primeiro_valor>segundo_valor
condicao2 = primeiro_valor<segundo_valor
condicao3 = primeiro_valor==segundo_valor


if condicao1:
    print (f'O valor {primeiro_valor} e maior do que {segundo_valor}')

elif condicao2:
    print (f'O valor {segundo_valor} e maior do que {primeiro_valor}')

elif condicao3:
    print (f'Os valores sao iguais')

else:
    print (f'Voce nao cumpriu com o que foi solicitado')


#Forma de resolução : Otávio Mirada

'''
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )
    
'''