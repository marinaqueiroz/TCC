# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 23:00:34 2016

@author: Marina
"""

import numpy as np
import numpy


#import time

qtdMat=3
ordem=2
ordemQuadrada=ordem**2
listaVetores=[]
matriz=[]
matrizes=[]


for j in range(qtdMat):
    for i in range(ordem):
        listaVetores.append(np.random.randn(ordem))
    matriz=numpy.matrix(listaVetores)
    matrizes.append(matriz)
    listaVetores.clear()   
    


# Criando um objeto do tipo file
for n in range (1,qtdMat+1):
    a=str(n)
    temp = open('mat'+a, 'w')
    b=matrizes[n-1]
    #trasnformando matriz para String
    c=str(b)
    #Escrevendo no arquivo 
    temp.write(c)
    #Fechando 
    temp.close()

#recuperando    
#temp=open("1")
#a= temp.read()
#print(a)


#x=matriz.transpose()
#print(x)
#y=matriz.trace()
#print("ok",y)
#print ("tempo=",time.clock())
