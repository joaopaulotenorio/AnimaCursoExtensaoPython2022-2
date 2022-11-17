# Aula 04 - D - 2022/11/16 

# Banco de Dados - Insert solicitando ao Usuário
# os dados de preenchimento e importando da função do arquivo C

########################
# Importando a Função de Conexão do Arquivo Main_C
import main_c as bd

conexao, cursor = bd.conectar()

# Solicitando as informações

nome = input("Informe o nome do herói/vilão: ")
nome_civil = input("Informe o nome civil do herói/vilão (sua identidade secreta): ")
tipo_numerico = input("Tecle 1 para Herói(na) ou 2 para Vilã(o): ")

# Consulta para o valor máximo usado no banco

sql = "SELECT MAX(pessoa_id)+1 FROM pessoas"
cursor.execute(sql)
pessoa_id = cursor.fetchone()[0]

if tipo_numerico == "1":
  tipo = "Herói(na)"
else:
  tipo = "Vilã(o)"

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"

# 5o. Passo: Executar o Comando SQL no SQLite (no cursor)
cursor.execute(sql)

# 6o. Passo: Confirmar o INSERT com o commit() e fechar o Banco de Dados
conexao.commit()
conexao.close()
