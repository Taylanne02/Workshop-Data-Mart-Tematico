
-- PERGUNTA 1
-- Como o faturamento varia ao longo do tempo?

SELECT 
    data_compra, 
    SUM(valor_compra) AS faturamento_total
FROM Fato_Transacoes
GROUP BY data_compra
ORDER BY data_compra;


-- PERGUNTA 2
-- Quais cidades concentram maior número de transações?

SELECT 
    Dim_Cliente.cidade, 
    COUNT(*) AS qtd_transacoes
FROM Fato_Transacoes
JOIN Dim_Cliente 
    ON Fato_Transacoes.id_cliente = Dim_Cliente.id_cliente
GROUP BY Dim_Cliente.cidade
ORDER BY qtd_transacoes DESC;


-- PERGUNTA 3
-- Quais cidades geram maior faturamento?

SELECT 
    Dim_Cliente.cidade, 
    SUM(valor_compra) AS faturamento_total
FROM Fato_Transacoes
JOIN Dim_Cliente 
    ON Fato_Transacoes.id_cliente = Dim_Cliente.id_cliente
GROUP BY Dim_Cliente.cidade
ORDER BY faturamento_total DESC;


-- PERGUNTA 4
-- Qual categoria de loja gera mais faturamento?

SELECT 
    Dim_Estabelecimento.categoria_loja, 
    SUM(valor_compra) AS faturamento_total
FROM Fato_Transacoes
JOIN Dim_Estabelecimento 
    ON Fato_Transacoes.id_estabelecimento = Dim_Estabelecimento.id_estabelecimento
GROUP BY Dim_Estabelecimento.categoria_loja
ORDER BY faturamento_total DESC;


-- PERGUNTA 5
-- Qual o valor médio das compras (ticket médio)?

SELECT 
    AVG(valor_compra) AS ticket_medio
FROM Fato_Transacoes;