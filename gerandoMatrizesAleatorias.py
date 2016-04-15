# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 23:00:34 2016

@author: Marina
"""

import numpy as np
import numpy
import sys
from scipy.io import savemat

#import time

#tam=1
ordem=3
ordemQuadrada=ordem**2
listaVetores=[]
matriz=[]
aux2=[]

for i in range(ordem):
    listaVetores.append(np.random.randn(ordem))
    
#for i in range(ordemQuadrada):
    #listaVetores.append(np.array(np.random.randn()))
   
    
#print(listaVetores)

for x in range(ordem):
    for y in range(ordem):
        a=listaVetores[x][y]
        aux2.append(a)
        #print(aux2)
        
    
#print("*****"+"****************************************************************")

matriz=numpy.matrix(listaVetores)
print("matriz","\n",matriz)
print(len(matriz))



# Criando um objeto do tipo file
for n in range (1,ordemQuadrada+1):
    a=str(n)
    temp = open('mat'+a, 'w')
    b=aux2[n-1]
    c=str(b)
    # Escrevendo no arquivo 
    temp.write(c)
    # Fechando 
    temp.close()

#recuperando    
temp=open("1")
a= temp.read()
print(a)



#x=matriz.transpose()
#print(x)
#y=matriz.trace()
#print("ok",y)
#print ("tempo=",time.clock())
