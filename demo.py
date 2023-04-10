#Realizando os imports
import numpy as np
import pandas as pd
from scipy.linalg import svd, diagsvd

#Criando o dataframe com os dados
df = pd.read_csv("ratings_small.csv")

# Cria a matriz
matriz = df.pivot_table(index='userId', columns='movieId', values='rating')
matriz = matriz.fillna(0)
A = matriz.values

# Exibe a matriz
print(A)


