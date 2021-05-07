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

    [ ] - Notícia de ultima hora! Descobrir a melhor solução com o custo benefício. Com
          esse dado final, definitivamente dominaremos o mercado de soluções de bolhas.
          Segue a lista de custo: .25, .27, .25, .25, .25, .25, .33, .31, .25, .29, .27,
                                  .22, .31, .25, .25, .33, .21, .25, .25, .25, .28, .25,
                                  .24, .22, .20, .25, .30, .25, .24, .25, .25, .25, .27,
                                  .25, .26, .29
"""

scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69, 34, 55, 51, 52, 44, 51, 69, 64,
          66, 55, 52, 61, 46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]

costs = [.25, .27, .25, .25, .25, .25, .33, .31, .25, .29, .27, .22, .31, .25, .25, .33,
         .21, .25, .25, .25, .28, .25, .24, .22, .20, .25, .30, .25, .24, .25, .25, .25,
         .27, .25, .26, .29]

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

cost = 100.0
mostEffective = 0
for i in range(len(bestSolution)):
    index = bestSolution[i]
    if cost > costs[index]:
        mostEffective = index
        cost = costs[index]
print('Solution', mostEffective, 'is the most effective with a cost of', costs[mostEffective])
