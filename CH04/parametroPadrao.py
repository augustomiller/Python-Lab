# Sempre colocar os parametros requeridos primeiro e depois os que contenham valores padrão.
def greet(name, msg='You rule!'):
    print('Hi', name + '.', msg)

greet('John')
greet('Jennifer', 'How are you today?')
    