import pandas as pd

# 1 - Trazendo o DataFrame de forma padrão (quando há muitas linhas, o pandas retorna as primeiras e últimas 5 linhas)
df = pd.read_csv("data.csv")

print(df)

# 1.2 - Como fazer com que todos os dados de um arquivo apareçam sem que o terminal 'pule' de linhas até o final:

print(df.to_string())

