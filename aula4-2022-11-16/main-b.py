# Aula 04 - B - 2022/11/16 

# Banco de Dados - Cont...

# 1o. Passo: Importar a biblioteca sqlite3
import sqlite3

# 2o. Passo: Vamos estabelecer uma
# Conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

# 3o. Passo: Criar um objeto do tipo cursor
cursor = conexao.cursor()

# 4o. Passo: Comando para inserir um Herói/Vilão
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"

# 5o. Passo: Executar o Comando SQL no SQLite (no cursor)
cursor.execute(sql)

# 6o. Passo: Confirmar o INSERT com o commit() e fechar o Banco
conexao.commit()
conexao.close()

