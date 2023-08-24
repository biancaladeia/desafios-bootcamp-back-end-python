'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor númerico.

Ex: n = leiaInt('Digite um n')

'''

def leiaInt(msg):
    try:
        n = int(input(msg))
    except (ValueError, TypeError):
        print('ERRO: por favor, digite um número inteiro válido.')
        return leiaInt(msg)
    else:
        return n

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')

