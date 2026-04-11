import pandas as pd
import sqlite3

print("1. [EXTRACT] Lendo os dados brutos...")
df_bruto = pd.read_csv('dados_brutos_cartao.csv')

print("2. [TRANSFORM] Limpando e gerando as Dimensões...")

# --- DIMENSÃO CANAL ---
df_canal = df_bruto[['Metodo_Pagamento', 'Descricao_Pagamento']].drop_duplicates().reset_index(drop=True)
df_canal.index += 1  # O índice começa em 1
df_canal.insert(0, 'id_canal', df_canal.index) # Insere a coluna de ID

# --- DIMENSÃO ESTABELECIMENTO ---
df_estabelecimento = df_bruto[['Nome_Loja', 'Categoria_Loja']].drop_duplicates().reset_index(drop=True)
df_estabelecimento.index += 1
df_estabelecimento.insert(0, 'id_estabelecimento', df_estabelecimento.index)

# --- DIMENSÃO TEMPO ---
df_tempo = df_bruto[['Data_Compra', 'Final_de_Semana']].drop_duplicates().reset_index(drop=True)
# Transformando a data 'YYYY-MM-DD' em um ID inteiro 'YYYYMMDD'
df_tempo.insert(0, 'id_tempo', df_tempo['Data_Compra'].str.replace('-', '').astype(int))

# --- DIMENSÃO CLIENTE ---
colunas_cliente = ['Nome_Cliente', 'Salario_Mensal', 'Score_Credito', 'Idade', 'Cidade', 'Estado']
df_cliente = df_bruto[colunas_cliente].drop_duplicates().reset_index(drop=True)
df_cliente.index += 1
df_cliente.insert(0, 'id_cliente', df_cliente.index)

print("3. [TRANSFORM] Cruzando IDs para montar a Tabela Fato...")
df_fato = df_bruto.copy()

# Trazendo os IDs para a tabela fato (equivalente a um PROCV/VLOOKUP)
df_fato = df_fato.merge(df_canal, on=['Metodo_Pagamento', 'Descricao_Pagamento'], how='left')
df_fato = df_fato.merge(df_estabelecimento, on=['Nome_Loja', 'Categoria_Loja'], how='left')
df_fato = df_fato.merge(df_cliente, on=colunas_cliente, how='left')
df_fato['id_tempo'] = df_fato['Data_Compra'].str.replace('-', '').astype(int)

# Mantendo apenas as colunas estruturadas da Tabela Fato
colunas_fato = ['id_cliente', 'id_estabelecimento', 'id_canal', 'id_tempo', 
                'Hora_Compra', 'Valor_Compra', 'Parcelas', 'Status_Pagamento']
df_fato = df_fato[colunas_fato]

# Renomeando as colunas para bater exatamente com o que criamos no tabelas.sql
df_fato.columns = ['id_cliente', 'id_estabelecimento', 'id_canal', 'id_tempo', 
                   'hora_compra', 'valor_compra', 'parcelas', 'status_pagamento']
df_cliente.columns = ['id_cliente', 'nome_cliente', 'salario_mensal', 'score_credito', 'idade', 'cidade', 'estado']
df_estabelecimento.columns = ['id_estabelecimento', 'nome_loja', 'categoria_loja']
df_canal.columns = ['id_canal', 'metodo_pagamento', 'descricao_pagamento']
df_tempo.columns = ['id_tempo', 'data_compra', 'final_de_semana']


print("4. [LOAD] Carregando os dados no banco SQLite...")
conn = sqlite3.connect('datamart_cartao.db')

# =========================================================
# NOVO: Limpando as tabelas antes de inserir novos dados
# =========================================================
cursor = conn.cursor()
cursor.executescript("""
    DELETE FROM Fato_Transacoes;
    DELETE FROM Dim_Cliente;
    DELETE FROM Dim_Estabelecimento;
    DELETE FROM Dim_Canal;
    DELETE FROM Dim_Tempo;
""")
# =========================================================

# O parâmetro if_exists='append' vai INSERIR os dados nas tabelas que o DDL já criou
df_cliente.to_sql('Dim_Cliente', conn, if_exists='append', index=False)
df_estabelecimento.to_sql('Dim_Estabelecimento', conn, if_exists='append', index=False)
df_canal.to_sql('Dim_Canal', conn, if_exists='append', index=False)
df_tempo.to_sql('Dim_Tempo', conn, if_exists='append', index=False)
df_fato.to_sql('Fato_Transacoes', conn, if_exists='append', index=False)

conn.commit()
conn.close()

print("ETL concluído com sucesso! Banco de dados populado.")