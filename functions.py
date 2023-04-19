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
    # verificando todos os campos que são diferentes de 0 (valor adicionado no lugar dos Nans).
    coordenadas = list(np.argwhere(matriz != 0))
    #listas com os ruidos colocados
    lista_ruidos_colocados = []
    #iteração pela quantidade de ruidos esperados
    for i in range(num_ruidos):
        if len(coordenadas) >= 1:
            #escolhe um numero de indice aleatório na lista de coordenadas
            n = randint(0,len(coordenadas)-1)
            #cordenada sorteada
            cord = coordenadas[n]
            #adiciona a coordenada na lista das coordenadas de ruidos
            lista_ruidos_colocados.append(coordenadas[n].tolist())
            #retira a coordenada adicionada acima da lista original
            coordenadas.pop(n)
            #adiciona um número aleatório no local determinado da matriz
            matriz[cord[0]][cord[1]] = randint(0,5)
    #retorna a matriz modificada e a lista das coordenadas nas quais os ruidos foram colocados.
    return matriz, lista_ruidos_colocados
