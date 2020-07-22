#code by @enedois_
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy
import random as rd
import math
distanciamentosocial = 3
badperson = bool(False)
lado = distanciamentosocial/2
total = 0

#fixed size array
#lista_loc_eixo_x = [-10,-5,0,5]
#lista_loc_eixo_y = [1,1,1,1]

#random array
lista_loc_eixo_x = []
lista_loc_eixo_y = []

#filling random array, change range number to add more points
for x in range(100):
    lista_loc_eixo_x.append(rd.randint(-100,100))
    lista_loc_eixo_y.append(rd.randint(-100,100))


#initializes figure
fig = plt.figure()

print("o distanciamento social definido é de",distanciamentosocial,"metros")

for x in range(len(lista_loc_eixo_x)):
    badperson = bool(False)
    cord = ("("+str(lista_loc_eixo_x[x])+","+str(lista_loc_eixo_y[x])+")")
    #print(cord)
    #print("Ponto(",lista_loc_eixo_x[x],",",lista_loc_eixo_y[x],")")
    for y in range(len(lista_loc_eixo_x)):
        distx = lista_loc_eixo_x[x]-lista_loc_eixo_x[y]
        disty = lista_loc_eixo_y[x]-lista_loc_eixo_y[y]
        disttotal = math.sqrt((distx**2)+ (disty**2))
        if not(disttotal==0):
            if disttotal <distanciamentosocial :
                badperson = bool(True)
                #print(cord,'esbarra em', distx, disty)
                print(cord,'esbarra em', lista_loc_eixo_x[y],",",lista_loc_eixo_y[y])
                total+=1
        #print("ponto(",lista_loc_eixo_x[y],",",lista_loc_eixo_y[y],")")


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
    color = "gray"
    if(badperson):
        color = "red"
    patch = patches.PathPatch(path, facecolor=color, lw=.5)
    ax.add_patch(patch)
    ax.set_xlim(-105,105)
    ax.set_ylim(-105,105)

print((total),"pessoas ultrapassaram o distanciamento social minimo")
plt.show()
    
