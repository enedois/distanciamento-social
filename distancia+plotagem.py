import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy
import random as rd

#prederteminated array
#lista_loc_eixo_x = [-10,-5,0,5]
#lista_loc_eixo_y = [1,1,1,1]

#random array
lista_loc_eixo_x = []
lista_loc_eixo_y = []

for x in range(100):
    lista_loc_eixo_x.append(rd.randint(-100,100))
    lista_loc_eixo_y.append(rd.randint(-100,100))


lado = 3/2
fig = plt.figure()

for x in range(len(lista_loc_eixo_x)):
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
    patch = patches.PathPatch(path, facecolor=numpy.random.rand(3,), lw=2)
    ax.add_patch(patch)
    ax.set_xlim(-100,100)
    ax.set_ylim(-100,100)


plt.show()
    
