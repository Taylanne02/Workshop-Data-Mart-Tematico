# ✒️ Workshop Data Mart de Transações de Cartões de Crédito


## 📖 Descrição


# Integrantes

* **Marcus Tavares Pires**
* **Taylanne Castelo Branco Cavalcante**
* **Yara Fernandes Ribeiro**
* **Yngrid Guimarães Silva**

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

## 🔗 Conexão Supabase com Power BI via ODBC

Pré-requisitos
* Conta ativa no Supabase.
* Power BI Desktop instalado (versão 64 bits recomendada).
* Credenciais do banco de dados (Host, DB Name, User, Port, Password).

🛠️ Passo 1: Download e Instalação do Driver
   * Para que o Windows entenda a linguagem do PostgreSQL, precisamos do driver psqlODBC.

	1- Acesse o repositório oficial: https://www.postgresql.org/ftp/odbc/releases/REL-18_00_0001-mimalloc/

	2- Localize e baixe o arquivo: psqlodbc_x64.msi (Versão 64 bits).

	3- Execute o instalador, clique em Next, aceite os termos e conclua a instalação padrão.

⚙️ Passo 2: Configuração do DSN no Windows (ODBC)
   * Agora vamos criar a "ponte" de conexão no sistema operacional.

	1- No menu iniciar do Windows, pesquise por "Configurar Fontes de Dados ODBC (64 bits)" e abra-o.

	2- Na aba DSN de Usuário, clique em Adicionar.

	3- Selecione o driver PostgreSQL Unicode(x64) e clique em Concluir.

	4- Na tela de configuração que abrir, preencha com os dados do seu Supabase:

		- Data Source: Supabase_ODBC (ou o nome que preferir).

		- Database: postgres.

		- Server: O endereço do host (ex: aws-0-xxxx.pooler.supabase.com).

		- Port: 5432 ou 6543.

		- User: postgres.

		- Password: Sua senha do banco de dados.


📊 Passo 3: Conexão com Power BI Desktop
	1- Abra o Power BI Desktop.

	2- Vá em Obter Dados > Mais... > pesquise por ODBC.

	3- No campo "Nome da fonte de dados (DSN)", selecione o nome que você criou (Supabase_ODBC).

	4- Se o Power BI pedir credenciais novamente:

		- Escolha a aba Banco de Dados.

		- Digite o usuário (postgres) e sua senha.

	5- No Navegador, selecione as tabelas desejadas (Fato_Transacoes, Dim_Cliente, etc.) e clique em Carregar.

## 🧪 Perguntas de Negócio (Queries SQL Documentadas)

* **1. Como o faturamento varia ao longo do tempo?**
  
SELECT 
    data_compra, 
    SUM(valor_compra) AS faturamento_total
FROM Fato_Transacoes
GROUP BY data_compra
ORDER BY data_compra;

* **2. Quais cidades concentram maior número de transações?**
  
SELECT 
    Dim_Cliente.cidade, 
    COUNT(*) AS qtd_transacoes
FROM Fato_Transacoes
JOIN Dim_Cliente 
    ON Fato_Transacoes.id_cliente = Dim_Cliente.id_cliente
GROUP BY Dim_Cliente.cidade
ORDER BY qtd_transacoes DESC;

* **3. Quais cidades geram maior faturamento?**
  
SELECT 
    Dim_Cliente.cidade, 
    SUM(valor_compra) AS faturamento_total
FROM Fato_Transacoes
JOIN Dim_Cliente 
    ON Fato_Transacoes.id_cliente = Dim_Cliente.id_cliente
GROUP BY Dim_Cliente.cidade
ORDER BY faturamento_total DESC;

* **4. Qual categoria de loja gera mais faturamento?**
  
SELECT 
    Dim_Estabelecimento.categoria_loja, 
    SUM(valor_compra) AS faturamento_total
FROM Fato_Transacoes
JOIN Dim_Estabelecimento 
    ON Fato_Transacoes.id_estabelecimento = Dim_Estabelecimento.id_estabelecimento
GROUP BY Dim_Estabelecimento.categoria_loja
ORDER BY faturamento_total DESC;

* **5. Qual o valor médio das compras (ticket médio)?**
  
SELECT 
    AVG(valor_compra) AS ticket_medio
FROM Fato_Transacoes;

## 👥 Desenvolvedores e suas Contribuições

* **Marcus Tavares Pires**
    * Geração dos dados com PythonFake 
    * Criação do banco de dados dos dados PythonFake
------------------------------

* **Taylanne Castelo Branco Cavalcante**
    * Criação da estrutura do banco de dados
    * Criação das Dashboard com POWERBI
    * Organização das dependências e instruções para execução do projeto
    * Organização do passo a passo para conectar o Supabase ao Power BI usando ODBC

------------------------------

* **Yara Fernandes Ribeiro**
    * Criação da develop
    * Organização do README
    * Organização do supabase e conexão dele com o código e com o Power bi 

------------------------------


* **Yngrid Guimarães Silva**  
    * Criação das perguntas
    * Organização power bi
    * Encrementação e alterações README

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
