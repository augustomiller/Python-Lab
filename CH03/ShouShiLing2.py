# Jogo pedra, papel e tesoura. 1.0.

import random

winner = ''

randomComputerChoice = ['rock', 'paper', 'scissors']
userChoice = input('rock, paper or scissors? ')

computerChoice = random.choice(randomComputerChoice)

print('You chose', userChoice, 'and the computer chose', computerChoice)
