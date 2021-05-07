# Jogo pedra, papel e tesoura. 1.0.

import random

winner = ''

# O randint retornara 0, 1 ou 2.
randomComputerChoice = random.randint(0, 2)

if randomComputerChoice == 0:
    computerChoice = 'rock'
elif randomComputerChoice == 1:
    computerChoice = 'paper'
else:
    computerChoice = 'scissors'

userChoice = ''
while (userChoice != 'rock' and
       userChoice != 'paper' and
       userChoice != 'scissors'):
    userChoice = input('rock, paper or scissors? ')


if computerChoice == userChoice:
    winner = 'Tie'
elif computerChoice == 'paper' and userChoice == 'rock':
    winner = 'Computer'
elif computerChoice == 'rock' and userChoice == 'scissor':
    winner = 'Computer'
elif computerChoice == 'scissor' and userChoice == 'paper':
    winner = 'Computer'
else:
    winner = 'User'

if winner == 'Tie':
    print('We both chose', computerChoice, ', play again.')
else:
    print(winner, 'won. The computer chose: -->', computerChoice, '.')
