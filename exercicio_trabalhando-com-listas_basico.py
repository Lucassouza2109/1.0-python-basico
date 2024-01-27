'''

Exercício
Exiba os indices da lista

0 Maria
1 Helena
2 Luiz
'''

# lista = ['Maria', 'Helena', 'Luiz']

# print(lista[0], lista[1], lista[2])

# lista2 = lista
# lista2[0] = 0
# lista2[1] = 1
# lista2[2] = 2
# print (lista2)

lista = ['Maria', 'Helena', 'Luiz']

i = 0
lista.append('João')

while i < len(lista):
    print(f'{i}, {lista[i]}')
    i += 1


"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))