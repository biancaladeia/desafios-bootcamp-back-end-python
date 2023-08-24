'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira. Considere a tabela de conversão abaixo:

Dólar Americano: R$ 4,91

Peso Argentino: R$ 0,02

Dólar Australiano: R$ 3,18

Dólar Canadense: R$ 3,64

Franco Suiço: R$ 0,42

Euro: R$ 5,36

Libra esterlina: R$ 6,21
'''

def conversor(valor, moeda):
    return valor / moeda

valor = float(input('Digite o valor em reais: '))
print(f'Com R$ {valor:.2f} você pode comprar: ')
print(f'US$ {conversor(valor, 4.91):.2f}')
print(f'ARS {conversor(valor, 0.02):.2f}')
print(f'AUD {conversor(valor, 3.18):.2f}')
print(f'CAD {conversor(valor, 3.64):.2f}')
print(f'CHF {conversor(valor, 0.42):.2f}')
print(f'EUR {conversor(valor, 5.36):.2f}')
print(f'GBP {conversor(valor, 6.21):.2f}')

