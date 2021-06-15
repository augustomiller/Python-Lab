# Função simples
def bark(name, weight):
    if weight > 20:
        print(name, 'says WOOF WOOF')
    else:
        print(name, 'says woof woof')

bark('Code', 40)
bark('Sparky', 9)
bark('Jackson', 12)
bark('Fido', 65)

# Função com retorno
def getBark(weight):
    if weight > 20:
        return 'says WOOF WOOF'
    else:
        return 'says woof woof'

codiesBark = getBark(40)
   
print("Codie's bark", codiesBark)