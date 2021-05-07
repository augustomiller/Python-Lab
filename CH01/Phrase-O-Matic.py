u"""
Programa 01.

Esse programa pega trêz listas de cada palavra, escolhe uma de cada lista
aleatóriamente, combina as palavras em uma frase (adequada para o slogan da
sua próxima startup) e exibe a frase.
"""

import random

verbs = ['Leverage', 'Sync', 'Target', 'Gamify', 'Offline', 'Crowd-sourced',
         '24/7', 'Learn-in', '30,000 foot']

adjectives = ['A/B Tested', 'Premium', 'Hyperlocal', 'Siloed', 'B-to-B',
              'Oriented', 'Cloud-based', 'API-based']

nouns = ['Early Adopter', 'Low-hanging Fruit', 'Pipeline', 'Splash Page',
         'Productivity', 'Process', 'Tipping Point', 'Paradigm']

# Escolhendo um verbo um adjetivo e um substantivo da respectiva lista.
verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)

# Criando uma frase "somando" as palavras
phrase = verb + '' + adjective + '' + noun

# Output da  frase
print(phrase)
