import pandas as pd
from faker import Faker
import random
from datetime import time

# Inicializa o Faker para o padrão brasileiro
fake = Faker('pt_BR')

# ---------------------------------------------------------
# 1. DICIONÁRIOS E LISTAS DE REFERÊNCIA
# ---------------------------------------------------------

cidades_reais = {
    'SP': ['São Paulo', 'Campinas', 'Santos', 'São José dos Campos'],
    'RJ': ['Rio de Janeiro', 'Niterói', 'Búzios', 'Petrópolis'],
    'MG': ['Belo Horizonte', 'Uberlândia', 'Ouro Preto'],
    'PR': ['Curitiba', 'Londrina', 'Maringá'],
    'SC': ['Florianópolis', 'Joinville', 'Blumenau'],
    'RS': ['Porto Alegre', 'Gramado', 'Caxias do Sul'],
    'BA': ['Salvador', 'Porto Seguro', 'Feira de Santana'],
    'PE': ['Recife', 'Olinda', 'Caruaru'],
    'DF': ['Brasília']
}

canais_info = {
    'Presencial': 'Venda física via maquininha no balcão da loja.',
    'Online': 'Compra realizada via site ou aplicativo próprio da marca.',
    'Link de Pagamento': 'URL gerada pelo vendedor e enviada por chat/rede social.'
}

categorias = ['Loja de Roupas', 'Eletrodomésticos', 'Restaurante', 'Farmácia', 'Supermercado', 'Livraria']

# ---------------------------------------------------------
# 2. FUNÇÃO GERADORA DE LINHAS (TRANSAÇÕES)
# ---------------------------------------------------------

def gerar_transacao():
    """Gera uma única transação de cartão de crédito estruturada como dicionário."""
    
    # Dados do Cliente
    estado_sigla = random.choice(list(cidades_reais.keys()))
    cidade_real = random.choice(cidades_reais[estado_sigla])
    
    # Canal e Regras de Horário
    metodo_pagamento = random.choice(list(canais_info.keys()))
    hora_gen = random.randint(8, 17) if metodo_pagamento == 'Presencial' else random.randint(0, 23)
    horario = time(hora_gen, random.randint(0, 59)).strftime('%H:%M')
    
    # Data
    data_aleatoria = fake.date_between(start_date='-1y', end_date='today')
    dia_num = data_aleatoria.weekday()
    is_fds = 'Sim' if dia_num >= 5 else 'Não'
    
    # Métricas Financeiras
    valor_compra = round(random.uniform(20.0, 3500.0), 2)
    parcelas = random.randint(1, 12) if valor_compra > 100 else 1 

    # Retorno estruturado (sem formatação de moeda para não quebrar o banco de dados)
    return {
        "Nome_Cliente": f"{fake.first_name()} {fake.last_name()}",
        "Salario_Mensal": round(random.uniform(1412.00, 25000.00), 2),
        "Score_Credito": random.randint(300, 1000),
        "Idade": random.randint(18, 80),
        "Cidade": cidade_real,
        "Estado": estado_sigla,
        "Metodo_Pagamento": metodo_pagamento,
        "Descricao_Pagamento": canais_info[metodo_pagamento],
        "Nome_Loja": fake.company(),
        "Categoria_Loja": random.choice(categorias),
        "Data_Compra": data_aleatoria.strftime('%Y-%m-%d'),
        "Hora_Compra": horario,
        "Final_de_Semana": is_fds,
        "Valor_Compra": valor_compra,
        "Parcelas": parcelas,
        "Status_Pagamento": random.choice(['Pago', 'Atrasado', 'Pendente'])
    }

# ---------------------------------------------------------
# 3. EXECUÇÃO E EXPORTAÇÃO
# ---------------------------------------------------------

if __name__ == "__main__":
    print("Iniciando a geração de dados...")

    # Define a quantidade de linhas desejadas
    NUM_REGISTROS = 10000

    # Executa a função repetidas vezes e guarda na lista
    lista_transacoes = [gerar_transacao() for _ in range(NUM_REGISTROS)]

    # Converte para DataFrame
    df_transacoes = pd.DataFrame(lista_transacoes)

    # Exporta para CSV
    nome_arquivo = 'dados_brutos_cartao.csv'
    df_transacoes.to_csv(nome_arquivo, index=False, encoding='utf-8')

    print(f"\nSucesso! Arquivo '{nome_arquivo}' gerado com {NUM_REGISTROS} linhas.")
    
    print("\nPrévia dos 5 primeiros registros:")
    print(df_transacoes.head())