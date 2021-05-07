print('#######################')
print('###### Exemplo 1 ######')
print('#######################')
# Exemplo 1
for i in range(5):
    print('Iterating ', i)


print(' ')
print('#######################')
print('###### Exemplo 2 ######')
print('#######################')
# Utilizando os itens da lista como indice.
smoothies = ['coconut', 'strawberry', 'banana', 'tropical', 'acai']
length = len(smoothies)
for i in range(length):
    print('Smoothies ', smoothies[i])



print(' ')
print('#######################')
print('###### Exemplo 3 ######')
print('#######################')
# Cria um intervalo de 5 até 10.
for i in range(5, 10):
    print(i)


print(' ')
print('#######################')
print('###### Exemplo 4 ######')
print('#######################')
# Podemos adicionar um passo: 2 para contar em incrementos
# Então cria uma sequencia começando de 3 e indo até 10, mas, contando em passos de 2.
for i in range(3, 10, 2):
    print(i)


print(' ')
print('#######################')
print('###### Exemplo 5 ######')
print('#######################')
# Podemos adicionar um passo: -1 para contar de traz para frente.
# Então cria uma sequencia começando de 10 e indo até 0.
for i in range(10, 0, -1):
    print(i)


print(' ')
print('#######################')
print('###### Exemplo 6 ######')
print('#######################')
# Podemos iniciar a partir de números negativos.
# Então cria uma sequencia começando de -10 e indo até 2.
for i in range(-10, 2):
    print(i)
