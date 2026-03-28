const sqlite3 = require("sqlite3").verbose();

const db = new sqlite3.Database("datamart_financas.db");

db.serialize(() => {
    // --- DIMENSÕES ---

    // Dimensão Cliente: Atributos demográficos e de crédito
    db.run(`
    CREATE TABLE IF NOT EXISTS dim_cliente (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        faixa_salarial TEXT,
        score_credito INTEGER,
        idade INTEGER,
        cidade TEXT,
        estado TEXT
    )
    `);

    // Dimensão Estabelecimento: Onde a compra ocorreu
    db.run(`
    CREATE TABLE IF NOT EXISTS dim_estabelecimento (
        id_estabelecimento INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_loja TEXT,
        categoria TEXT, -- Ex: Restaurante, Farmácia, Viagem
        tipo_estabelecimento TEXT -- Ex: Franquia, Loja Local
    )
    `);

    // Dimensão Canal: Meio de pagamento
    db.run(`
    CREATE TABLE IF NOT EXISTS dim_canal (
        id_canal INTEGER PRIMARY KEY AUTOINCREMENT,
        metodo TEXT -- Ex: Presencial, Online, Link de Pagamento
    )
    `);

    // Dimensão Tempo: Essencial para análise de séries temporais
    db.run(`
    CREATE TABLE IF NOT EXISTS dim_tempo (
        id_tempo INTEGER PRIMARY KEY AUTOINCREMENT,
        data_completa DATE,
        ano INTEGER,
        mes INTEGER,
        dia INTEGER,
        dia_da_semana TEXT,
        eh_final_de_semana INTEGER, -- 0 para Não, 1 para Sim
        periodo_dia TEXT -- Ex: Manhã, Tarde, Noite, Madrugada
    )
    `);

    // --- TABELA FATO ---

    // Fato Transações: Contém as chaves estrangeiras e as métricas numéricas
    db.run(`
    CREATE TABLE IF NOT EXISTS fato_transacoes (
        id_transacao INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INTEGER,
        id_estabelecimento INTEGER,
        id_canal INTEGER,
        id_tempo INTEGER,
        valor_compra REAL,
        qtd_parcelas INTEGER,
        valor_iof REAL,
        valor_cashback REAL,
        status_pagamento TEXT, -- Ex: Pago, Atrasado (para cálculo de inadimplência)
        FOREIGN KEY (id_cliente) REFERENCES dim_cliente(id_cliente),
        FOREIGN KEY (id_estabelecimento) REFERENCES dim_estabelecimento(id_estabelecimento),
        FOREIGN KEY (id_canal) REFERENCES dim_canal(id_canal),
        FOREIGN KEY (id_tempo) REFERENCES dim_tempo(id_tempo)
    )
    `);

});

module.exports = db;