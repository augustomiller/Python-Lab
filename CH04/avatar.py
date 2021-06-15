# 

def getAttribute(query, default):

    question = query + ' [' + default + ']? '
    answer = input(question)
    if (answer == ''):
        answer = default
        
    print('You chose', answer)
    return answer

    #Criando as chamadas para cada atributo.
    hair = getAttribute('What hair color', 'brown')
    hairLength = getAttribute('What hair length', 'short')
    eye = getAttribute('What eye color', 'blue')
    gender = getAttribute('What gender', 'female')
    glasses = getAttribute('Has glasses', 'no')
    beard = getAttribute('Has beard', 'no')