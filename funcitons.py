import pandas as pd
import numpy as np
from random import randint

def introduzRuido(dataframe_inicial, num_ruidos):
    
    # verificando todos os campos que são diferentes de NaN
    nao_nulos = dataframe_inicial.notnull().stack()
    campos_nao_nulos = nao_nulos[nao_nulos].index.tolist()
    lista_ruidos_colocados = []
    for i in range(num_ruidos):
        if len(campos_nao_nulos) >= 1:
            n = randint(0,len(campos_nao_nulos)-1)
            cord = campos_nao_nulos[n]
            lista_ruidos_colocados.append(campos_nao_nulos[n])
            campos_nao_nulos.pop(n)
            dataframe_inicial.loc[cord[0],cord[1]] = randint(0,5)

    return dataframe_inicial, lista_ruidos_colocados

    # lista_random = [randint(0,len(campos_nao_nulos)) for i in range(num_ruidos)]
    # for rd in lista_random:
    #     campos_nao_nulos_final.append(campos_nao_nulos[rd])
    # for valor in campos_nao_nulos_final:
    #     dataframe_inicial.loc[valor[0],valor[1]] = randint(0,5)
    # inserindo os novos valores nas coordenadas selecionadas


# data = {'coluna1': ['A', 'A', 'B', 'B'], 'coluna2': ['x', 'y', 'x', 'y'], 'valor': [1, 2, 3, 4]}
# df = pd.DataFrame(data).pivot(index='coluna1', columns='coluna2', values='valor')
# print(df)

# df = introduzRuido(df,2)
# print(df)