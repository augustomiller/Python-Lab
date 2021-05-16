"""

Programa que decompõe número de centenas, dezenas e unidades

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
usuário a valor do saque e depois informar quantas notas de cada valor serão
fornecidas.

As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Módulo divmod()
Toma dois números (não complexos) como argumentos e devolve um par de números
que consiste em seu quociente e restante ao usar a divisão inteira. Com tipos
de operandos mistos, as regras para operadores aritméticos binários se aplicam.
Para números inteiros, o resultado é o mesmo que (a // b, a % b). Para números
de ponto flutuante, o resultado é (q, a % b), onde q geralmente é math.floor(a / b),
mas pode ser 1 a menos que isso. Em qualquer caso, q * b + a % b está muito próximo
de a, se a % b é diferente de zero, tem o mesmo sinal que b e 0 <= abs(a % b) < abs(b).
"""

saque = 299

init = 0

nota1 = nota5 = nota10 = nota50 = nota100 = init

nota100, saque = divmod(saque, 100)
nota50, saque = divmod(saque, 50)
nota10, saque = divmod(saque, 10)
nota5, nota1 = divmod(saque, 5)

if nota100 > 0:
    print(f'{nota100} nota(s) de 100')
if nota50 > 0:
    print(f'{nota50} nota(s) de 50')
if nota10 > 0:
    print(f'{nota10} nota(s) de 10')
if nota5 > 0:
    print(f'{nota5} nota(s) de 5')
if nota1 > 0:
    print(f'{nota1} nota(s) de 1')

