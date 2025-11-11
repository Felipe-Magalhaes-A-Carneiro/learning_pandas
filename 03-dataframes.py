import pandas as pd

# 1 - Criando um Data Frame no pandas:

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print(df)

print("-" * 40)

# 2 - Usando o index é possível retornar os dados de uma linha:

print(df.loc[0])

print("-" * 40)

# 2.2 - Retornando mais de um index (perceba o uso de dois colchetes):
print(df.loc[[0, 1]])

print("-" * 40
      )
# 3 - Assim como no Series, podemos definir o nome / tipo do index em DataFrames:

df = pd.DataFrame(data, index = ["Day 1", "Day 2", "Day 3"])

print(df)

print("-" * 40)