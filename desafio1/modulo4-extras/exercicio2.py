# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 80,00 por dia e R$ 0,20 por km rodado.

km_percorridos = float(input('Digite a quantidade de km percorridos: '))
dias_alugados = int(input('Digite a quantidade de dias alugados: '))

preco_a_pagar = (km_percorridos * 0.20) + (dias_alugados * 80)

print(f'O preço a pagar é R$ {preco_a_pagar:.2f}')

