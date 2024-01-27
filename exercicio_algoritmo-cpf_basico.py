
import random # random = aleatório
import sys

nove_dígitos = '' # vai armazenar os 9 números gerados automaticamente pelo random . 
i = 0
while i <= 8: # vai iterar 9 vezes (0-8), gerando os nove_dígitos 
    nove_dígitos += str (random.randint (0,9)) # nove_dígitos = os 9 dígitos gerados aleatoriamente pelo random.randint \
                                               # gera números aleatórios inteiros . 
    i += 1

print (f' Os 9 primeiros dígitos sao: {nove_dígitos}') 


# for i in range(len(cpf)):
#     resultado = cpf[i] * contagem[i]
#     print(resultado, end = ',')

i = 0 # criado um indice para iterar no loop.
contagem_1 = 10 # contagem determinada na introdução do exercício .
soma_multiplicação = 0
cpf = nove_dígitos 

while i <= 8:

    resultado = int(cpf [i]) * contagem_1 # multiplicação dos indices do CPF (transformei o CPF que estava em string) * CONTAGEM
    contagem_1 -=1 # inserção do contador de forma que a contagem fique decrescente . 
    i += 1  # inserção do contador para eliminar o loop infinito
    soma_multiplicação += resultado    # a soma da multiplicação = a soma do resultado 

#print(f'\n O resultado da soma = {soma_multiplicação}') # Simplesmente solicito o print do resultado da soma 

vezes_dez = soma_multiplicação * 10 # crio uma variavel 
#print (f' O resultado da soma *10 = {vezes_dez}') # print da variavel 

resto_da_divisão = vezes_dez % 11 # crio uma variavel
#print (f' O resto da divisão /11 = {resto_da_divisão}') # realizo uma operação direta

resultado_anterior = resto_da_divisão # crio uma variavel 
primeiro_digito = resultado_anterior if resultado_anterior <9 else 0 # crio uma condicional de 1 linha
print (f' O primeiro digito do CPF = {primeiro_digito}') # print do valor 


############################################################################################################################


#print (f' A soma dos 9 primeiros dígitos + Primeiro digito = {soma_multiplicação + primeiro_digito}')

i = 0 # indice igual a 0 para iterar no loop while . 
contagem_2 = 11 # contagem determinada na introdução do exercício . 
soma_multiplicação = 0
cpf = nove_dígitos + str(primeiro_digito) #simplesmente concatenei o nove_dígitos + primeiro_digito


while i <= 9: # foi adicionada +1 passagem no loop devido ao acréscimo do primeiro digito a conta . 

    resultado = int(cpf [i]) * contagem_2 # multiplicação dos indices do CPF (transformei o CPF que estava em string) * CONTAGEM
    contagem_2 -=1 # inserção do contador de forma que a contagem fique decrescente . 
    i += 1  # inserção do contador para eliminar o loop infinito
    soma_multiplicação += resultado    # a soma da multiplicação = a soma do resultado 

#print(f'\n O resultado da soma = {soma_multiplicação}') # Simplesmente solicito o print do resultado da soma 

vezes_dez = soma_multiplicação * 10 # crio uma variavel 
#print (f' O resultado da soma *10 = {vezes_dez}') # print da variavel 

resto_da_divisão = vezes_dez % 11 # crio uma variavel
#print (f' O resto da divisão /11 = {resto_da_divisão}') # realizo uma operação direta

resultado_anterior = resto_da_divisão # crio uma variavel 
segundo_digito = resultado_anterior if resultado_anterior <9 else 0 # crio uma condicional de 1 linha
#print (f' O segundo digito do CPF = {segundo_digito}') # print do valor 


print (f' {nove_dígitos}{primeiro_digito}{segundo_digito}')