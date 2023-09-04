# Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para cada opção, crie uma função. Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversão correta.

def celsius_para_fahrenheit(celsius):
    return celsius * 1.8 + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

def menu():
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    opcao = int(input("Digite a opção desejada: "))
    return opcao

opcao = menu()

if opcao == 1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    print(f"{celsius}ºC é igual a {celsius_para_fahrenheit(celsius)}ºF")

elif opcao == 2:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    print(f"{fahrenheit}ºF é igual a {fahrenheit_para_celsius(fahrenheit)}ºC")

else:
    print("Opção inválida")

