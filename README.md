# ✒️ Workshop Data Mart de Transações de Cartões de Crédito


## 📖 Descrição


# Integrantes

* **Marcus Tavares Pires**
* **Taylanne Castelo Branco Cavalcante**
* **Yara Fernandes Ribeiro**
* **Yngrid Guimarães Silva**

## 📂 Estrutura do Projeto

## 📦 Dependências necessárias

Para instalar todas as dependências necessárias, execute:

```bash
pip install -r requirements.txt
```

## 🚀 Como Rodar o Projeto

1️⃣ Gerar os dados brutos
```bash
cd gerador_de_dados/dados
python gerador_de_dados.py
```

Isso vai criar o arquivo dados_brutos_cartao.csv.

2️⃣ Criar o banco de dados
```bash
cd ../database
python criar_banco.py
```

Isso vai gerar o arquivo datamart_cartao.db.

3️⃣ Executar o ETL
```bash
cd ../etl
python etl.py
```

O script vai extrair, transformar e carregar os dados do CSV para o banco.

## 🧪 Perguntas de Negócio (Queries SQL Documentadas)

## 👥 Desenvolvedores e suas Contribuições

* **Marcus Tavares Pires**
    * Geração dos dados com PythonFake 
    * Criação do banco de dados dos dados PythonFake
------------------------------

* **Taylanne Castelo Branco Cavalcante**
    * Criação da estrutura do banco de dados
    * Criação power bi

------------------------------

* **Yara Fernandes Ribeiro**
    * Criação da develop
    * Organização do README

------------------------------


* **Yngrid Guimarães Silva**  
    * Criação das perguntas
    * Organização power bi
    * Encrementação README

------------------------------

# Data Mart – Análise de Transações
Este projeto tem como objetivo desenvolver um Data Mart dimensional para análise de transações financeiras, permitindo identificar padrões de consumo, comportamento de clientes e desempenho dos canais de pagamento.

Tecnologias:
- Python
- SQLite
- Power BI

Modelo Dimensional: 
O modelo segue o padrão Star Schema.

Tabela Fato:
- Fato_Transacoes

Dimensões:
- Dim_Cliente
- Dim_Canal
- Dim_Estabelecimento
- Dim_Tempo

Granularidade:
Cada registro representa uma transação realizada por um cliente em um determinado canal, data e estabelecimento.

ETL:
Os dados foram extraídos de arquivos CSV, transformados utilizando Python e carregados em um banco SQLite estruturado em modelo dimensional.

Perguntas de Negócio:
1. Como o faturamento varia ao longo do tempo?
2. Quais cidades concentram maior número de transações?
3. Quais cidades geram maior faturamento?
4. Qual categoria de loja gera mais faturamento?
5. Qual o valor médio das compras (ticket médio)?

As consultas SQL correspondentes estão no arquivo `sql/perguntas_negocio.sql`.

Dashboard: 
O dashboard foi desenvolvido no Power BI, apresentando indicadores principais, análise por canal, evolução temporal e comportamento das transações.

Como executar: 
1. Executar os scripts ETL
2. Gerar o banco de dados SQLite
3. Abrir o arquivo Power BI (.pbix)
