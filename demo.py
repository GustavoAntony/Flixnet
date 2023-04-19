import pandas as pd
import numpy as np
from random import randint

def introduzRuido(dataframe_inicial, num_ruidos):
    
    # verificando todos os campos que são diferentes de NaN
    nao_nulos = dataframe_inicial.notnull().stack()
    campos_nao_nulos = nao_nulos[nao_nulos].index.tolist()
    campos_nao_nulos_final = []
    lista_random = [randint(0,len(campos_nao_nulos)) for i in range(num_ruidos)]
    novos_valores = np.full_like(dataframe_inicial.values, randint(0,5))
    for rd in lista_random:
        campos_nao_nulos_final.append(campos_nao_nulos[rd])
    # inserindo os novos valores nas coordenadas selecionadas
    dataframe_inicial.values[campos_nao_nulos_final] = novos_valores[campos_nao_nulos_final]

    return dataframe_inicial


df = pd.read_csv("ratings_small.csv")
matriz = df.pivot_table(index='userId', columns='movieId', values='rating')

print(introduzRuido(matriz, 2))