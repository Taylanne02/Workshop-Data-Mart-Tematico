-- ==========================================
-- SCRIPT DDL: CRIAÇÃO DO DATA MART
-- ==========================================

-- 1. CRIAÇÃO DAS TABELAS DIMENSÃO

CREATE TABLE Dim_Cliente (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_cliente VARCHAR(100) NOT NULL,
    salario_mensal DECIMAL(10,2),
    score_credito INTEGER,
    idade INTEGER,
    cidade VARCHAR(100),
    estado CHAR(2)
);

CREATE TABLE Dim_Estabelecimento (
    id_estabelecimento INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_loja VARCHAR(150) NOT NULL,
    categoria_loja VARCHAR(50)
);

CREATE TABLE Dim_Canal (
    id_canal INTEGER PRIMARY KEY AUTOINCREMENT,
    metodo_pagamento VARCHAR(50) NOT NULL,
    descricao_pagamento TEXT
);

CREATE TABLE Dim_Tempo (
    id_tempo INTEGER PRIMARY KEY,
    data_compra DATE NOT NULL,
    final_de_semana VARCHAR(3)
);

-- 2. CRIAÇÃO DA TABELA FATO

CREATE TABLE Fato_Transacoes (
    id_transacao INTEGER PRIMARY KEY AUTOINCREMENT,  -- <--- ESTA LINHA É A QUE FALTA
    id_cliente INTEGER NOT NULL,
    id_estabelecimento INTEGER NOT NULL,
    id_canal INTEGER NOT NULL,
    id_tempo INTEGER NOT NULL,
    hora_compra TIME,
    valor_compra DECIMAL(10,2) NOT NULL,
    parcelas INTEGER DEFAULT 1,
    status_pagamento VARCHAR(20),
    
    FOREIGN KEY (id_cliente) REFERENCES Dim_Cliente(id_cliente),
    FOREIGN KEY (id_estabelecimento) REFERENCES Dim_Estabelecimento(id_estabelecimento),
    FOREIGN KEY (id_canal) REFERENCES Dim_Canal(id_canal),
    FOREIGN KEY (id_tempo) REFERENCES Dim_Tempo(id_tempo)
);
