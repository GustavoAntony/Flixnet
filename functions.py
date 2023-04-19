import pandas as pd
import numpy as np
from random import randint

def comprimir (u, s, vt, K):
    """Remove elementos de u, s e vt deixando somente K componentes restantes
    """ 
    u_ = u[:,0:K]
    s_ = s[:K]
    vt_ = vt[:K,:]
    return u_, s_, vt_

def introduzRuido(matriz, num_ruidos):
    # verificando todos os campos que são diferentes de NaN
    coordenadas = list(np.argwhere(matriz != 2.5))
    lista_ruidos_colocados = []
    for i in range(num_ruidos):
        if len(coordenadas) >= 1:
            n = randint(0,len(coordenadas)-1)
            cord = coordenadas[n]
            lista_ruidos_colocados.append(coordenadas[n].tolist())
            coordenadas.pop(n)
            matriz[cord[0]][cord[1]] = randint(0,5)
    return matriz, lista_ruidos_colocados

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