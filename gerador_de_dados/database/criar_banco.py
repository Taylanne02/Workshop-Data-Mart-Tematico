import sqlite3
import os

print("Conectando ao banco de dados...")
# Isso vai criar um arquivo chamado 'datamart_cartao.db' na sua pasta
conn = sqlite3.connect('datamart_cartao.db')
cursor = conn.cursor()

# Pega o caminho da pasta onde o SEU SCRIPT (.py) está guardado
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Junta essa pasta com o nome do arquivo SQL
caminho_sql = os.path.join(diretorio_atual, 'tabelas.sql')

print("Lendo o script DDL...")
# Abre e lê aquele arquivo tabelas.sql que criamos no passo anterior
with open(caminho_sql, 'r', encoding='utf-8') as f:
    script_ddl = f.read()

print("Criando as tabelas...")
# Executa os comandos SQL dentro do banco de dados
cursor.executescript(script_ddl)

# Salva e fecha a conexão
conn.commit()
conn.close()

print("Sucesso! Banco de dados estruturado e pronto para uso.")