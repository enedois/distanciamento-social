#code by @enedois_
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np
import random as rd
import math

qtdofindividuals = 100
axisize = 200
distanciamentosocial = 3
results = []

#fixed size array
#lista_loc_eixo_x = [-10,-5,0,5]
#lista_loc_eixo_y = [1,1,1,1]

#random array
lista_loc_eixo_x = []
lista_loc_eixo_y = []

###filling random array with qtdofindividuals positions, change range number to add more people
##for x in range(qtdofindividuals):
##    lista_loc_eixo_x.append(rd.randint(0,axisize))
##    lista_loc_eixo_y.append(rd.randint(0,axisize))


#initializes figure
#fig = plt.figure()

print("Distanciamento social definido é de",distanciamentosocial,"metros")
   
for range100 in range(0,100):
    fig = plt.figure()
    lista_loc_eixo_x=[]
    lista_loc_eixo_y=[]
    for x in range(qtdofindividuals):
        lista_loc_eixo_x.append(rd.randint(0,axisize))
        lista_loc_eixo_y.append(rd.randint(0,axisize))
    badperson = bool(False)
    total = 0
    badperson = bool(False)
    lado = 1
    total = 0    
      
    for x in range(len(lista_loc_eixo_x)):
        badperson = bool(False)
        cord = ("("+str(lista_loc_eixo_x[x])+","+str(lista_loc_eixo_y[x])+")")
        #print(cord)
        #print("Ponto(",lista_loc_eixo_x[x],",",lista_loc_eixo_y[x],")")
        for y in range(len(lista_loc_eixo_x)):
            cord2 = ("("+str(lista_loc_eixo_x[y])+","+str(lista_loc_eixo_y[y])+")")
            if not(cord == cord2):        
                #print("Compararando", cord,"com",cord2)
                distx = lista_loc_eixo_x[x]-lista_loc_eixo_x[y]
                disty = lista_loc_eixo_y[x]-lista_loc_eixo_y[y]
                disttotal = math.sqrt((distx**2)+ (disty**2))      
                if not(disttotal==0):
                    if disttotal <distanciamentosocial :
                        badperson = bool(True)                     
                        #print(cord,'tocou',cord2)
                        total+=1      


        verts = [
        (lista_loc_eixo_x[x]-lado,lista_loc_eixo_y[x]-lado), # left, bottom
        (lista_loc_eixo_x[x]-lado,lista_loc_eixo_y[x]+lado), # left, top
        (lista_loc_eixo_x[x]+lado,lista_loc_eixo_y[x]+lado), # right, top
        (lista_loc_eixo_x[x]+lado,lista_loc_eixo_y[x]-lado), # right, bottom
        (0., 0.), # ignored
        ]
        codes = [Path.MOVETO,
                 Path.LINETO,
                 Path.LINETO,
                 Path.LINETO,
                 Path.CLOSEPOLY,
                 ]
        path = Path(verts, codes)
        ax = fig.add_subplot(111)
        color = "black"
        if(badperson):
            color = "red"
        patch = patches.PathPatch(path, facecolor=color, lw=.5)
        ax.add_patch(patch)
        ax.set_xlim(0-2,axisize+2)
        ax.set_ylim(0-2,axisize+2)

    results.append((total/qtdofindividuals))
    print((total),"pessoas ultrapassaram o distanciamento social minimo")
    print((total/qtdofindividuals)*100,"% das pessoas não cumpriram o distanciamento")
    print(np.mean(results))
    print(np.mean(results)<0.10)
    plt.savefig(str(range100)+"_"+str(qtdofindividuals)+"_"+".png")
    print("Iteração:",range100)
print("Rodadas",len(results),"iterações")
print("Pior Resultado:",np.amax(results)*100)
print("Melhor Resultado:",np.amin(results)*100)
print("Média:",np.mean(results)*100)
print(results)
