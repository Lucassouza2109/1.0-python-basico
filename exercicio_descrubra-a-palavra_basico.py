"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

#Informar ao usuário que ele esta dentro de um jogo

import os

palavra_secreta = 'amor'
letras_acertadas = ''
numero_tentativas = 0
print ('Voce acaba de iniciar um jogo de Palavra secreta')

while True:
    letra_digitada = input ('Digite uma letra e tente adivinhar a palavra: ') .lower ()
    # captura a letra digitada.
    numero_tentativas += 1
    # contabiliza o numero de tentativas.

    if len(letra_digitada) > 1 : # para caso o usuário digite + de 1 letra.
        print ('Favor digitar apenas uma letra por vez')
        continue # uma vez identificado o erro, volta ao inicio do loop.
    
    if letra_digitada in palavra_secreta: # se a letra digitada estiver contida na palavra secreta.
        letras_acertadas += letra_digitada # a letra acertada sera composta pela letra digitada.


    palavra_formada = ''
    for letra_inserida in palavra_secreta: # Caso a letra inserida esteja contida na palavra secreta. 
        if letra_inserida in letras_acertadas: # se a letra inserida estiver contida nas letras acertadas.
            palavra_formada += letra_inserida # a palavra formada vai armazenar a letra inserida. 
        else:
            palavra_formada += '*' # se a letra inserida não estiver contida na palavra secreta complementa a palavra formada com *.
    
    print ('Palavra formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system ('clear')
        print ('VOCE GANHOU!! PARABENS!') 
        print ('A palavra era', palavra_secreta)
        print ('Tentativas:', numero_tentativas) 

        break


        

