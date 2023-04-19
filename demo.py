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
    print(i)
    #Introduz o ruido
    B = copy.deepcopy(A)
    B, coordenada_ruido = introduzRuido(B,1)
    coordenada_ruido = coordenada_ruido[0]
    

    u, s, vt = svd(B)

    u_, s_, vt_ = comprimir(u,s,vt,100)
    B2 = u_ @ np.diag(s_) @ vt_ 




    erros.append(abs(B2[coordenada_ruido[0],coordenada_ruido[1]] - A[coordenada_ruido[0],coordenada_ruido[1]]))



df_erros = pd.DataFrame({
    "erro": erros
})


df_erros.to_csv("erros_gu3.csv", index=False)



