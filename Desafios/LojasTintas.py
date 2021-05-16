"""
Faça um Programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de
3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
Comprar apenas latas de 18 litros;
Comprar apenas galões de 3,6 litros;
Misturar latas e galões, de forma que o custo da tinta seja menor. Acrescente 10%
de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
import math

print('')
# Área a ser pintada em metros quadrados.
areaToBePainted = int(input('Qual o tamanho da área a ser pintada em metros quadrados: ')) 
litersPerMeter = 6
literPerCan = 18

slackArea = areaToBePainted * 1.1 # Adicionar 10% é só multiplicar por 1.1
litersToBeUsed = slackArea / litersPerMeter
numberOfCans = math.ceil(litersToBeUsed / literPerCan)
valueWithCans = numberOfCans * 80 # Valor se a compra for apenas latas de 18 litros.
print(f'Você deverá usar {numberOfCans} latas de 18 litros, no valor de R${valueWithCans}')

litersPerGallon = 3.6
numberOfGallon = math.ceil(litersToBeUsed / litersPerGallon)
valueWithGallon = numberOfGallon * 25 # Valor se a compra for apenas em galões de 3.6 litros.
print(f'Você deverá usar {numberOfGallon} galões de 3.6 litros, no valor de R${valueWithGallon}')

# Compra de tinta otimizado por valor
numberOfCans = math.floor(litersToBeUsed / literPerCan)
valueWithCans = numberOfCans * 80
missingLiters = (litersToBeUsed % literPerCan)
numberOfGallon = math.ceil(missingLiters / litersPerGallon)
valueWithGallon = numberOfGallon * 25

totalValue = valueWithCans + valueWithGallon
print(f'Ou você pode usar {numberOfCans} latas de 18 litros mais {numberOfGallon} galão de 3.6 litros no valor de R${totalValue}')
print('')