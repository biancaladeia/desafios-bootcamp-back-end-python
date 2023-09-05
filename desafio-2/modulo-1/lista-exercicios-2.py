# Classe abstrata que representa um cliente do banco
class Cliente:
    # Construtor da classe Cliente
    def __init__(self, nome, telefone, renda_mensal):
        self.nome = nome # Propriedade que armazena o nome do cliente
        self.telefone = telefone # Propriedade que armazena o telefone do cliente
        self.renda_mensal = renda_mensal # Propriedade que armazena a renda mensal do cliente

    # Método abstrato que retorna o valor do cheque especial do cliente
    def get_cheque_especial(self):
        pass

# Classe que representa um cliente mulher, herda da classe Cliente
class ClienteMulher(Cliente):
    # Método que retorna o valor do cheque especial da cliente mulher, igual à sua renda mensal
    def get_cheque_especial(self):
        return self.renda_mensal

# Classe que representa um cliente homem, herda da classe Cliente
class ClienteHomem(Cliente):
    # Método que retorna o valor do cheque especial do cliente homem, zero por enquanto
    def get_cheque_especial(self):
        return 0

# Classe que representa uma conta corrente do banco
class ContaCorrente:
    # Construtor da classe ContaCorrente
    def __init__(self, clientes):
        self.clientes = clientes # Propriedade que armazena uma lista de clientes titulares da conta
        self.saldo = 0 # Propriedade que armazena o saldo da conta
        self.operacoes = [] # Propriedade que armazena uma lista de operações de saques e depósitos

    # Método que retorna o valor máximo que a conta pode ficar negativa, baseado no cheque especial dos clientes
    def get_limite_negativo(self):
        limite = 0
        for cliente in self.clientes:
            limite -= cliente.get_cheque_especial()
        return limite

    # Método que realiza um saque na conta, se houver saldo ou cheque especial suficiente
    def sacar(self, valor):
        if valor > 0 and self.saldo - valor >= self.get_limite_negativo():
            self.saldo -= valor
            self.operacoes.append(('Saque', -valor))
            print('Saque realizado com sucesso.')
        else:
            print('Saldo insuficiente.')

    # Método que realiza um depósito na conta, se o valor for positivo
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.operacoes.append(('Depósito', valor))
            print('Depósito realizado com sucesso.')
        else:
            print('Valor inválido.')

    # Método que imprime o extrato da conta, mostrando o saldo e as operações realizadas
    def imprimir_extrato(self):
        print('Extrato da conta:')
        for operacao in self.operacoes:
            print('{}: R$ {:.2f}'.format(operacao[0], operacao[1]))
        print('Saldo: R$ {:.2f}'.format(self.saldo))
