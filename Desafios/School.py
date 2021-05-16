"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa
deve calcular a média alcançada por aluno e apresentar:

A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
https://docs.python.org/pt-br/3/library/functions.html
"""

defaultAverage = 7
partialNoteFirstSemester = float(input('Digite a primeira nota: '))
partialNoteSecondSemester = float(input('Digite a segunda nota: '))

studantAverage = (partialNoteFirstSemester + partialNoteSecondSemester) / 2

print(f'Sua média é : {studantAverage}')

if studantAverage == 10:
    print(f'Aluno aprovado com distinção')
elif studantAverage >= defaultAverage:
    print(f'Aluno aprovado')
else:
    print(f'Aluno reprovado')
