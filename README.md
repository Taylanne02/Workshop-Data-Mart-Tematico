# ✒️ Workshop Data Mart de Transações de Cartões de Crédito


## 📖 Descrição


# Integrantes

* **Marcus Tavares Pires**
* **Taylanne Castelo Branco Cavalcante**
* **Yara Fernandes Ribeiro**
* **Yngrind Guimarães Silva**

## 📂 Estrutura do Projeto

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

------------------------------

* **Yara Fernandes Ribeiro**
    * Criação da develop
    * Organização do README

------------------------------


* **Yngrind Guimarães Silva**  
