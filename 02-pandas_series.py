import pandas as pd

# 1- crição de uma série (series) unidimensional de qualquer tipo:
a = [1, 7, 2]

var = pd.Series(a)

print(var)

# 2- acessando os rótulos (labels) de uma série (assim como em uma lista):

print(var[1])

# 3- Criando labels - com index, você pode definir qual será os id's das suas linhas: 

var = pd.Series(a, index = ["x", "y", "z"])

print(var)

# acessando a label pelo index alterado:

print(var["z"])

# 4 - Key/values sendo Objetos e tratados como Series

calories = {"Day 1": 420, "Day 2": 380, "Day 3": 390}

var_calories = pd.Series(calories)

print(var_calories)

# 4.2 - Criando series usando informação do "Day 1" e "Day 2"

var_calories = pd.Series(calories, index = ["Day 1","Day 2"])

print(var_calories)

# 5 - DataFrames

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print(df)