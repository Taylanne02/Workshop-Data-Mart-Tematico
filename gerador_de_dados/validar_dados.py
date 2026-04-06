import sqlite3
import pandas as pd
import os

# Conecta ao banco de dados
caminho_db = os.path.join('database', 'datamart_cartao.db')
conn = sqlite3.connect(caminho_db)

print("\n" + "="*50)
print("🔍 INICIANDO VALIDAÇÃO DAS PERGUNTAS DE NEGÓCIO")
print("="*50)

# 1. Receita por Categoria de Loja
query1 = """
SELECT e.categoria_loja, ROUND(SUM(f.valor_compra), 2) AS faturamento_total
FROM Fato_Transacoes f
JOIN Dim_Estabelecimento e ON f.id_estabelecimento = e.id_estabelecimento
GROUP BY e.categoria_loja
ORDER BY faturamento_total DESC LIMIT 3;
"""
print("\n1. Top 3 Categorias de Lojas (Faturamento):")
print(pd.read_sql_query(query1, conn))

# 2. Risco de Inadimplência por Canal
query2 = """
SELECT c.metodo_pagamento, COUNT(f.id_transacao) AS qtd_compras_atrasadas
FROM Fato_Transacoes f
JOIN Dim_Canal c ON f.id_canal = c.id_canal
WHERE f.status_pagamento = 'Atrasado'
GROUP BY c.metodo_pagamento
ORDER BY qtd_compras_atrasadas DESC;
"""
print("\n2. Compras Atrasadas por Método de Pagamento:")
print(pd.read_sql_query(query2, conn))

# 3. Comportamento no Final de Semana
query3 = """
SELECT t.final_de_semana AS e_final_de_semana, ROUND(AVG(f.valor_compra), 2) AS ticket_medio
FROM Fato_Transacoes f
JOIN Dim_Tempo t ON f.id_tempo = t.id_tempo
GROUP BY t.final_de_semana;
"""
print("\n3. Ticket Médio (Final de Semana vs Dias Úteis):")
print(pd.read_sql_query(query3, conn))

# 4. Consumo e Score por Estado
query4 = """
SELECT c.estado, ROUND(SUM(f.valor_compra), 2) AS volume_total_gasto, CAST(AVG(c.score_credito) AS INTEGER) AS media_score
FROM Fato_Transacoes f
JOIN Dim_Cliente c ON f.id_cliente = c.id_cliente
GROUP BY c.estado
ORDER BY volume_total_gasto DESC LIMIT 5;
"""
print("\n4. Top 5 Estados por Volume Gasto e Score Médio:")
print(pd.read_sql_query(query4, conn))

# 5. Uso do Parcelamento por Faixa Etária
query5 = """
SELECT 
    CASE 
        WHEN c.idade BETWEEN 18 AND 25 THEN '1. 18-25 anos'
        WHEN c.idade BETWEEN 26 AND 40 THEN '2. 26-40 anos'
        WHEN c.idade BETWEEN 41 AND 60 THEN '3. 41-60 anos'
        ELSE '4. Acima de 60 anos'
    END AS faixa_etaria,
    ROUND(AVG(f.parcelas), 1) AS media_parcelas
FROM Fato_Transacoes f
JOIN Dim_Cliente c ON f.id_cliente = c.id_cliente
GROUP BY faixa_etaria
ORDER BY faixa_etaria;
"""
print("\n5. Média de Parcelas por Faixa Etária:")
print(pd.read_sql_query(query5, conn))

conn.close()
print("\n" + "="*50)
print("✅ VALIDAÇÃO CONCLUÍDA")
print("="*50 + "\n")