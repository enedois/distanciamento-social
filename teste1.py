import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy

lista_loc_eixo_x = [3,1,4,2]
lista_loc_eixo_y = [2,2,5,4]

lado = 3/2
fig = plt.figure()

for x in range(len(lista_loc_eixo_x)):
    verts = [
    (x-lado,lista_loc_eixo_y[x]-lado), # left, bottom
    (x-lado,lista_loc_eixo_y[x]+lado), # left, top
    (x+lado,lista_loc_eixo_y[x]+lado), # right, top
    (x+lado,lista_loc_eixo_y[x]-lado), # right, bottom
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
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)


plt.show()
    
