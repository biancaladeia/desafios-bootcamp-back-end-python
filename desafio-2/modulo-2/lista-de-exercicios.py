# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).

import sqlite3
conexao = sqlite3.connect('exercicio.db')
c = conexao.cursor()

c.execute('CREATE TABLE alunos (id INT, nome VARCHAR(100), idade INT, curso VARCHAR(20))')

conexao.commit()
conexao.close()

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

# Inserindo o primeiro aluno
c.execute("INSERT INTO alunos VALUES (1, 'João', 20, 'Engenharia')")

# Inserindo o segundo aluno
c.execute("INSERT INTO alunos VALUES (2, 'Maria', 22, 'Medicina')")

# Inserindo o terceiro aluno
c.execute("INSERT INTO alunos VALUES (3, 'Pedro', 21, 'Direito')")

# Inserindo o quarto aluno
c.execute("INSERT INTO alunos VALUES (4, 'Ana', 19, 'Engenharia')")

# Inserindo o quinto aluno
c.execute("INSERT INTO alunos VALUES (5, 'Miguel', 23, 'Administração')")

# Salvando as alterações e fechando a conexão
conexao.commit()
conexao.close()

'''
3. Consultas Básicas
Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecionar todos os registros da tabela "alunos".
b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
c) Selecionar os alunos do curso de "Engenharia" em ordem
alfabética.
d) Contar o número total de alunos na tabela '''

# a) Selecionar todos os registros da tabela "alunos"
c.execute("SELECT * FROM alunos")
print("a) Todos os registros da tabela:")
print(c.fetchall())

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos
c.execute("SELECT nome, idade FROM alunos WHERE idade > 20")
print("\nb) Alunos com mais de 20 anos:")
print(c.fetchall())

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética
c.execute("SELECT * FROM alunos WHERE curso = 'Engenharia' ORDER BY nome")
print("\nc) Alunos de Engenharia em ordem alfabética:")
print(c.fetchall())

# d) Contar o número total de alunos na tabela
c.execute("SELECT COUNT(*) FROM alunos")
total_alunos = c.fetchone()[0]
print(f"\nd) Total de alunos na tabela: {total_alunos}")

conexao.close()

'''
4. Atualização e Remoção
a) Atualize a idade de um aluno específico na tabela.
b) Remova um aluno pelo seu ID.'''

# a) Atualizar a idade de um aluno específico na tabela
c.execute("UPDATE alunos SET idade = ? WHERE id = ?", (23, 2))

# b) Remover um aluno pelo seu ID
c.execute("DELETE FROM alunos WHERE id = ?", (4,))

# Exibir os registros atualizados
c.execute("SELECT * FROM alunos")
print("Registros após a atualização e remoção:")
print(c.fetchall())

# Fechar a conexão
conexao.commit()  # Salvar as alterações
conexao.close()

'''
5. Criar uma Tabela e Inserir Dados
Crie uma tabela chamada "clientes" com os campos: id (chave
primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
registros de clientes na tabela.
'''

# Criar a tabela "clientes"
c.execute('CREATE TABLE clientes (id INT, nome VARCHAR(100), idade INT, saldo FLOAT)')

# Inserir registros de clientes
clientes = [
    (1, 'João', 30, 1000.50),
    (2, 'Maria', 25, 500.75),
    (3, 'Pedro', 35, 1500.25),
    (4, 'Ana', 28, 2000.0),
    (5, 'Miguel', 40, 300.0)
]

c.executemany("INSERT INTO clientes VALUES (?, ?, ?, ?)", clientes)

# Salvar as alterações e fechar a conexão
conexao.commit()
conexao.close()


'''
6. Consultas e Funções Agregadas
Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecione o nome e a idade dos clientes com idade superior a
30 anos.
b) Calcule o saldo médio dos clientes.
c) Encontre o cliente com o saldo máximo.
d) Conte quantos clientes têm saldo acima de 1000.'''


# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos
c.execute("SELECT nome, idade FROM clientes WHERE idade > 30")
print("a) Clientes com mais de 30 anos:")
print(c.fetchall())

# b) Calcule o saldo médio dos clientes
c.execute("SELECT AVG(saldo) FROM clientes")
media_saldo = c.fetchone()[0]
print(f"\nb) Saldo médio dos clientes: {media_saldo}")

# c) Encontre o cliente com o saldo máximo
c.execute("SELECT * FROM clientes ORDER BY saldo DESC LIMIT 1")
cliente_max_saldo = c.fetchone()
print(f"\nc) Cliente com saldo máximo: {cliente_max_saldo}")

# d) Conte quantos clientes têm saldo acima de 1000
c.execute("SELECT COUNT(*) FROM clientes WHERE saldo > 1000")
total_clientes_saldo_maior_1000 = c.fetchone()[0]
print(f"\nd) Total de clientes com saldo acima de 1000: {total_clientes_saldo_maior_1000}")

# Fechar a conexão
conexao.close()

