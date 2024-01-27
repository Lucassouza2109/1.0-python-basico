"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

# Produtos = ''
# lista_de_compra = []

# while True:
#     print('Selecione uma opção:')
#     opção_inicial = (input(f'[i]nserir [a]pagar [l]istar: '))
#     print (opção_inicial)

#     if opção_inicial == "":
#         print ('Nada para listar, selecione uma Opção')
#         continue

#     if opção_inicial == 'i':
#         produto = (input(f'Valor: '))

#     if produto in lista_de_compra:
#         lista_de_compra += produto


#     lista = ''
#     for produto in lista_de_compra:
#         if produto in lista_de_compra:
#             lista += produto
    
#     else:
#         print ('Existe um erro no produto inserido')

#     print ('lista')


"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
lista = []

while True: #1. definiu inicialmente os prints iniciais.
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ') # Mediante a opcao inserida se e detalhado o condigo abaixo em 5 fases. 

################################################

    if opcao == 'i': #2. Se a opção selecionada for 'i'.
        os.system('clear') #3. Importou o modulo os, e solicitou para que quando digitasse 'i', limpasse o sistema. 
        valor = input('Valor: ') #3. Input do Valor = Produto da lista.
        lista.append(valor) #3. solicita para que o Valor imputado seja armazenado no fim (end) da lista.

################################################

    elif opcao == 'a': #2. Se a opção selecionada for 'a'.
        indice_str = input('Escolha o índice para apagar: ') #5. Sendo selecionado o 'a', escolha qual o indice a ser apagado.
        
        try:
            indice = int(indice_str) #5. Verifica se o valor imputado corresponde a um numero inteiro.
            del lista[indice] #5. Se sim, deleta esse indice da lista 
        except ValueError: #5. Se nao, trata os possíveis erros. 
            print('Por favor digite número int.') #5. Printa o erro.  
        except IndexError: #5. Se nao, trata os possíveis erros. 
            print('Índice não existe na lista') #5. Printa o erro.  
        except Exception: #5. Se nao, trata os possíveis erros. 
            print('Erro desconhecido') #5. Printa o erro. 

################################################

    elif opcao == 'l': #2. Se a opção selecionada for 'l'.
        os.system('clear') #4. Importou o modulo os, e solicitou para que quando digitasse 'l', limpasse o sistema.

        if len(lista) == 0: #4. Se o tamanho da lista for igual a 0, imprimi = Nada para lista.
            print('Nada para listar')

        for i, valor in enumerate(lista): #4. Havendo a inserção de produtos eles serão exibidos em indice e Valor
            print(i, valor) #4. Imprime essa estrutura. 

################################################  
    
    else:
        print('Por favor, escolha i, a ou l.') #2. Se a opção selecionada na for: a, i ou l.
    



