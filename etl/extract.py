from faker import Faker
import pandas as pd
import random

#Estrutura base

fake = Faker('pt_BR')

dados = []

for i in range(1000):
    dados.append({
        "nome": fake.name(),
        "idade": random.randint(18,70),
        "valor_compra": round(random.uniform(10,2000),2)
    })


pd.DataFrame(dados).to_csv("../data/raw_data.csv", index=False)