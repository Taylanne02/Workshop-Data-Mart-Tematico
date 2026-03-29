from faker import Faker
import random
from datetime import time

# Inicializa o Faker para o padrão brasileiro
fake = Faker('pt_BR')

def formatar_real(valor):
    return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

# Lista de cidades reais por estado para garantir coerência absoluta
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

print("--- GERANDO DADOS REAIS E FORMATADOS ---\n")

# 1. Dados do Cliente
nome_limpo = f"{fake.first_name()} {fake.last_name()}"
salario_mensal = round(random.uniform(1412.00, 25000.00), 2)

# Escolhe um estado e uma cidade real daquele estado
estado_sigla = random.choice(list(cidades_reais.keys()))
cidade_real = random.choice(cidades_reais[estado_sigla])

print(f"Nome: {nome_limpo}")
print(f"Salário Mensal: {formatar_real(salario_mensal)}")
print(f"Score de Crédito: {random.randint(300, 1000)}")
print(f"Idade: {random.randint(18, 80)}")
print(f"Cidade/Estado: {cidade_real} - {estado_sigla}") # Agora 100% coerente

print("-" * 30)

# 2. Canal e Descrição
canais_info = {
    'Presencial': 'Venda física via maquininha no balcão da loja.',
    'Online': 'Compra realizada via site ou aplicativo próprio da marca.',
    'Link de Pagamento': 'URL gerada pelo vendedor e enviada por chat/rede social.'
}
metodo_pagamento = random.choice(list(canais_info.keys()))
print(f"Método: {metodo_pagamento}")
print(f"Descrição: {canais_info[metodo_pagamento]}")

print("-" * 30)

# 3. Estabelecimento
categorias = ['Loja de Roupas', 'Eletrodomésticos', 'Restaurante', 'Farmácia', 'Supermercado', 'Livraria']
print(f"Loja: {fake.company()}")
print(f"Categoria: {random.choice(categorias)}")

print("-" * 30)

# 4. Regras de Horário e Tempo
data_aleatoria = fake.date_between(start_date='-1y', end_date='today')

if metodo_pagamento == 'Presencial':
    hora_gen = random.randint(8, 17)
else:
    hora_gen = random.randint(0, 23)

minuto_gen = random.randint(0, 59)
horario_formatado = time(hora_gen, minuto_gen).strftime('%H:%M')

dias_pt = {0: "Segunda-feira", 1: "Terça-feira", 2: "Quarta-feira", 
           3: "Quinta-feira", 4: "Sexta-feira", 5: "Sábado", 6: "Domingo"}
dia_num = data_aleatoria.weekday()
dia_nome = dias_pt[dia_num]

status_fds = f"Sim, {dia_nome}" if dia_num >= 5 else f"Não, {dia_nome}"

print(f"Data: {data_aleatoria.strftime('%d/%m/%Y')} às {horario_formatado}")
print(f"É Final de Semana? {status_fds}")

print("-" * 30)

# 5. Métricas Financeiras
valor_compra = round(random.uniform(20.0, 3500.0), 2)
print(f"Valor da Compra: {formatar_real(valor_compra)}")
print(f"Parcelas: {random.randint(1, 12)}")
print(f"Status: {random.choice(['Pago', 'Atrasado', 'Pendente'])}")