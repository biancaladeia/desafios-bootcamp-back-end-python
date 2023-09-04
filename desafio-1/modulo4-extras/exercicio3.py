'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário.

Se o salário for até R$ 1000,00 o funcionário terá 20% de aumento.

Entre R$ 1001,00 até R$ 2800,00 o funcionário terá 10% de aumento.

Acima de R$ 2801,00 o funcionário terá 5% de aumento.

'''

def aumento(salario):
    if salario <= 1000:
        return salario * 1.2
    elif salario <= 2800:
        return salario * 1.1
    else:
        return salario * 1.05
    
salario = float(input('Digite o salário: '))
print(f'O novo salário é R$ {aumento(salario):.2f}')

