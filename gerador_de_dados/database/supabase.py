import sqlite3
import pandas as pd
import urllib.parse
from sqlalchemy import create_engine

# --- CONFIGURAÇÕES DO SUPABASE ---
USER = 'postgres'
PASSWORD = 'senhaforte45*'
HOST = 'db.crfxjckihwmaewvtybqb.supabase.co'
PORT = '5432'
DB_NAME = 'postgres'

# Tratamento da senha para evitar erro de caracteres especiais
password_safe = urllib.parse.quote_plus(PASSWORD)
supabase_url = f'postgresql://{USER}:{password_safe}@{HOST}:{PORT}/{DB_NAME}'
engine_supabase = create_engine(supabase_url)

# --- CONEXÃO COM O BANCO LOCAL ---
DB_LOCAL = 'datamart_cartao.db'

print(f"--- Iniciando migração do banco: {DB_LOCAL} ---")

try:
    conn_sqlite = sqlite3.connect(DB_LOCAL)
    cursor = conn_sqlite.cursor()

    # 1. Pega o nome de todas as tabelas que existem no seu arquivo .db
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
    tabelas = [row[0] for row in cursor.fetchall()]

    if not tabelas:
        print("Aviso: Nenhuma tabela encontrada no banco local.")
    else:
        print(f"Tabelas encontradas: {tabelas}")

    # 2. Migra tabela por tabela
    for tabela in tabelas:
        print(f"Migrando conteúdo da tabela: {tabela}...")
        
        # Lê tudo o que está dentro da tabela local
        df = pd.read_sql_query(f"SELECT * FROM {tabela}", conn_sqlite)
        
        if df.empty:
            print(f"A tabela {tabela} está vazia, mas a estrutura será criada.")

        # Envia para o Supabase
        # 'replace' cria a tabela lá com os mesmos nomes de coluna e dados
        df.to_sql(tabela, engine_supabase, if_exists='replace', index=False)
        print(f"Tabela {tabela} (com {len(df)} linhas) enviada com sucesso!")

    conn_sqlite.close()
    print("\n--- Migração concluída! Todas as tabelas estão no Supabase. ---")

except Exception as e:
    print(f"Erro durante a migração: {e}")