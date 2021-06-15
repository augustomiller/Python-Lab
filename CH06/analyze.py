"""
Calcula legibilidade 1.0

Este programa analisa um texto e retorna o resultado em um indice de facilidade
de leitura para um publico alvo de acordo com a tabela de Rudolph Flesch.
 __________________________________________________________________________________
| Indice       | Nível Escolar     | Notas                                         |
 ----------------------------------------------------------------------------------
| 100,00-90,00 | 5 ano (5th grade) | Muito fácil de compreender, aluno 11 anos     |
 ----------------------------------------------------------------------------------
| 90,0-80,0    | 6 ano (6th grade) | Fácil de ler - coloquial para consumidores    |
 ----------------------------------------------------------------------------------
| 80,0-70,0    | 7 ano (7th grade) | Razoavelmente fácil de ler                    |
 ----------------------------------------------------------------------------------
| 70,0-60,0    | 7 e 9 ano         | Compreendido por adolescentes de 13 a 15 anos |
 ----------------------------------------------------------------------------------
| 60,0-50,0    | 1 - 3 ano         | Razoavelmente difícil de ler                  |
-----------------------------------------------------------------------------------
| 50,0-30,0    | Universitario     | Difícil de ler                                |
 ----------------------------------------------------------------------------------
| 30,0-10,0    | Graduado          | Muito difícil de ler, mas bem-compreendido por|
|              |                   | universitarios e graduados                    |
 ----------------------------------------------------------------------------------
| 10,0-0,0     | Universitario     | Extremamente difícil de ler.                  |
 ----------------------------------------------------------------------------------

Formula para calcular a legibilidade:
    206,835-1,015( totalDePalavras / totalDeFrases ) -84,6( totalDeSilabas / totalDePalavras )

https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests

Todo:
[x] Extrair todas as palavras para uma lista.
[x] Contar quantas palavras a lista tem.

[x] Calcular o numero de frases no texto.

[] Calcular o numero de silabas, (heuristica).
    [x] Se uma palavra tem menos de tres caracteres, e contada como uma silaba.
    [x] Caso contrario, contaremos o numero de vogais, que representarão o numero de silabas.
    [x] Para que o passo anterior seja mais exato, removemos quaisquer vogais consecutivas em uma palavra.
    [x] Removendo os e finais das palavras para nao contar os mudos.
    [ ] Tratamos o caractere y como uma vogal se estiver no final da palavra.


"""


import ch1text


# retorna o numero total de silabas de todas as palavras.
def count_syllables(words):
    count = 0

    for word in words:
        word_count = count_syllables_in_word(word)
        count = count + word_count
        
    return count

# Retorna o numero de silabas de uma única palavra.
def count_syllables_in_word(word):
    count = 0

    endings = '.,;!?:-'
    last_chair = word[-1]

    if last_chair in endings:
        processed_word = word[0:-1]
    else:
        processed_word = word

    if len(processed_word) <= 3:
        return 1

    if processed_word[-1] in 'eE':
        processed_word = processed_word[0:-1]

    vowels = "aeiouAEIOU"
    prev_char_was_vowel = False

    for char in processed_word:
        if char in vowels:
            if not prev_char_was_vowel:
                count = count + 1
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False

    if processed_word[-1] in 'yY':
        count = count + 1

    return count

def count_sentences(text):
    count = 0

    terminals = '.;?!'

    for char in text:
        if char in terminals:
            count = count + 1

    return count

def output_results(score):
    if score >= 90:
        print('Reading level of 5th Grade')
    elif score >= 80:
        print('Reading level of 6th Grade')
    elif score >= 70:
        print('Reading level of 7th Grade')
    elif score >= 60:
        print('Reading level of 8-9th Grade')
    elif score >= 50:
        print('Reading level of 10-12th Grade')        
    elif score >= 30:
        print('Reading level of college Student')        
    else:
        print('Reading level of college Graduate')

def compute_readability(text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0

    words = text.split()
    total_words = len(words)
    total_sentences = count_sentences(text)
    total_syllables = count_syllables(words) 

    score = (206.835 - 1.015 * (total_words / total_sentences) 
                       -84.6 * (total_syllables / total_words))

    # print(total_words, 'words')
    # print(total_sentences, 'sentences')
    # print(total_syllables, 'sillables')
    # print(score, 'reading ease score')
    output_results(score)

compute_readability(ch1text.text)