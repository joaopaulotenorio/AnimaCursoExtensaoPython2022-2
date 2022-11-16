# Aula 04 - A - 2022/11/16 

# Acessando Banco de Dados

# 1o. Passo: Importar a biblioteca sqlite3
import sqlite3

# 2o. Passo: Vamos estabelecer uma
# Conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

# 3o. Passo: Criar um objeto do tipo cursor
cursor = conexao.cursor()

# 4o. Passo: Comando SQL do Banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

# 5o. Passo: Executar o Comando SQL no SQLite (no cursor)
cursor.execute(sql)

# 6o. Passo: Exibir a Consulta com todos os nomes de Heróis e Vilões do Banco de Dados
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)

print("\n")
for pessoa in pessoas:
  print(f"Nome: {pessoa[1]} ( {pessoa[3]} )")

# 7o. Passo: 

  
# 8o. Passo: 

