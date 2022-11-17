# Aula 04 - C - 2022/11/16 

# Banco de Dados - Função de Conexão para o Banco de Dados

# 1o. Passo: Importar a biblioteca sqlite3
import sqlite3

# Transformando os passos 2 e 3 em Função
def conectar():

  # 2o. Passo: Vamos estabelecer uma
  # Conexão com o banco de dados
  conexao = sqlite3.connect("dc_universe.db")
  
  # 3o. Passo: Criar um objeto do tipo cursor
  cursor = conexao.cursor()

  return conexao, cursor
