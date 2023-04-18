import pandas as pd
import numpy as np
from random import randint

def introduzRuido(dataframe_inicial, num_ruidos):
    lista_ruidos = [randint(0,5) for i in range(num_ruidos)]
    # verificando todos os campos que são diferentes de NaN
    nao_nulos = dataframe_inicial.notnull().stack()
    campos_nao_nulos = nao_nulos[nao_nulos].index.tolist()

    # exibindo a lista de campos não nulos
    print(campos_nao_nulos)
    return lista_ruidos


df = pd.read_csv("ratings_small.csv")
matriz = df.pivot_table(index='userId', columns='movieId', values='rating')

print(introduzRuido(matriz, 2))