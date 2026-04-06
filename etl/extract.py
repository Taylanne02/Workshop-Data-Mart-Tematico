from faker import Faker
import random

fake = Faker('pt_BR')

dados = []

for _ in range(1000):

    data = fake.date_time_this_year()

    registro = {
        # cliente
        "nome": fake.name(),
        "idade": random.randint(18,70),
        "cidade": fake.city(),
        "estado": fake.estado_sigla(),
        "faixa_salarial": random.choice(["Baixa","Média","Alta"]),
        "score_credito": random.randint(300,900),

        # estabelecimento
        "nome_loja": fake.company(),
        "categoria": random.choice(["Restaurante","Farmácia","Viagem"]),
        "tipo_estabelecimento": random.choice(["Franquia","Local"]),

        # canal
        "metodo": random.choice(["Online","Presencial","Link"]),

        # tempo
        "data": data,

        # fato
        "valor_compra": round(random.uniform(10,1000),2),
        "qtd_parcelas": random.randint(1,12),
        "valor_iof": round(random.uniform(0,20),2),
        "valor_cashback": round(random.uniform(0,30),2),
        "status_pagamento": random.choice(["Pago","Atrasado"])
    }

    dados.append(registro)

for d in dados[:5]:
    print(d)