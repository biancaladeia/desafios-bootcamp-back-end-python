# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(numero1, numero2, numero3):
    return numero1 + numero2 + numero3

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

resultado = soma(numero1, numero2, numero3)

print(f"A soma dos números é {resultado}")

