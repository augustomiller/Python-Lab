"""
Bubbles_R-Us Inc

As pesquisas contínua da empresa Bubbles_R-Us Inc garantem que as várias máquinas
de bolhas espalhadas por várias partes do páis produzam as melhores bolhas de sabão.

Hoje eles estão testando uma nova amostragem o "fator bolhas" de inúmeras formulações
diferentes de sua solução nova de bolhas de sabão. Ou seja estão testando quantas bolhas
podem ser produzidas a partir de uma determinada solução.

O que a empresa Bubbles_R-Us Inc precisa que voçê desenvolva:

    [x] - Como receberam vários testes novos de bolhas, eles precisam de um sistema que liste
      as novas soluções e seus escores correspondentes. Ex: 'Bubble Solution #0 score: 60'
      Os novos escores: 60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69, 34, 55, 51, 52,
                        44, 51, 69, 64, 66, 55, 52, 61, 46, 31, 57, 52, 44, 18, 41, 53,
                        55, 61, 51, 44

    [x] - Preciso visualizar o numero total de scores de bolhas. Ex: 'Bubbles tests: 36'

    [x] - Preciso visualizar o numero de escore mais alto. Ex: 'Highest bubble score: 69'

    [x] - Preciso visualizar cada solução que conteve o mesmo valor de escore mais alto.
"""

scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69, 34, 55, 51, 52, 44, 51, 69, 64,
          66, 55, 52, 61, 46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]

highScore = 0

length = len(scores)
for i in range(length):
    print('Bubble solution #' + str(i), 'score:', scores[i])
    
    if scores[i] > highScore:
        highScore = scores[i]

print('Bubbles tests: ', length)
print('Highest bubble score: ', highScore)

bestSolution = []
for i in range(length):
    if highScore == scores[i]:
        bestSolution.append(i)

print('Solutions with highest score: ', bestSolution)
