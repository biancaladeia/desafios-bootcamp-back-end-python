# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).

import sqlite3
conexao = sqlite3.connect('exercicio.db')
c = conexao.cursor()

c.execute('CREATE TABLE alunos (id INT, nome VARCHAR(100), idade INT, curso VARCHAR(20))')

conexao.commit()
conexao.close()

