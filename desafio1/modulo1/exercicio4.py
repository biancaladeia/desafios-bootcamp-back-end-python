# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input('Informe o valor da sua hora de trabalho: '))
horas_trabalhadas = float(input('Informe a quantidade de horas trabalhadas no mês: '))
salario = valor_hora * horas_trabalhadas
print(f'O seu salário no mês é de R$ {salario:.2f}')

