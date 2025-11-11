import pandas as pd

# 1 - Criando um Data Frame no pandas:

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print(df)

# 2 - Usando o index é possível retornar os dados de uma linha:

print(df.loc[0])