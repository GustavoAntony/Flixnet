#Realizando os imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import copy
from scipy.linalg import svd, diagsvd
from functions import *

#Criando o dataframe com os dados
df = pd.read_csv("ratings_small.csv")

#Cria a matriz inicial
A = df.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)
A = A.values

erros = []




for i in range(100):
    #Introduz o ruido
    matriz_com_ruido, coordenada_ruido = introduzRuido(A,1)
    coordenada_ruido = coordenada_ruido[0]
    
    #Cria a matriz sem NaN's
    B = copy.deepcopy(matriz_com_ruido)

    u, s, vt = svd(B)

    u_, s_, vt_ = comprimir(u,s,vt,10)
    B2 = u_ @ np.diag(s_) @ vt_ 




    erros.append(abs(B2[coordenada_ruido[0],coordenada_ruido[1]] - A[coordenada_ruido[0],coordenada_ruido[1]]))



df_erros = pd.DataFrame({
    "erro": erros
})


df_erros.to_csv("erros2.csv", index=False)



