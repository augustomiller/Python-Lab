print('##############################################################')
print('###### Exemplo 1 - Adicionando itens há uma lista vazia.######')
print('##############################################################')

# criando uma lista vazia.
listaDeCoisas = []

#adicionando itens há uma lista vazia.
listaDeCoisas.append('Lápis')
listaDeCoisas.append('Borracha')
listaDeCoisas.append('Apontador')
print(listaDeCoisas)




print(' ')
print('#######################')
print('###### Mistério #######')
print('#######################')

mystery = ['secret'] * 33
print(mystery)




print(' ')
print('#####################################################')
print('###### Exemplo 2 - Deletando item de uma lista ######')
print('#####################################################')
# Deletando um item de uma lista.

lista = ['secret1', 'secret2', 'secret3', 'secret4']
print('Total: ', lista)
del lista[1]
print('Total: ', lista)



print(' ')
print('#####################################################################')
print('###### Exemplo 3 - Adicionando uma lista dentro de outra lista ######')
print('#####################################################################')

listaOne = ['a', 'b', 'c']
listaTwo = ['d', 'e', 'f']
listaTwo.extend(['g', 'h', 'i'])

listaOne.extend(listaTwo)

print(listaOne)




print(' ')
print('######################################################')
print('###### Exemplo 4 - Inserindo item em uma lista. ######')
print('######################################################')

lista = ['a', 'b', 'c']

# Primeiro parâmetro é o indice onde deseja inserir o dado.
lista.insert(1, 'z')

print(lista)