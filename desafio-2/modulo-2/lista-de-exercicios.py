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

