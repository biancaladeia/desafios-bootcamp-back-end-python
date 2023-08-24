# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso(numero):
    numero = str(numero)
    return numero[::-1]

numero = int(input("Digite um número: "))

resultado = reverso(numero)

print(f"O reverso do número é {resultado}")

