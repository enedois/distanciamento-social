#verifica se um numero n de pontos com coordenadas x,y ultrapassaram o distanciamento social minimo definido
import math
lista_loc_eixo_x = [0,2,12,13]
lista_loc_eixo_y = [1,3,5,7]
total = 0
distanciamentosocial = 3
badperson = false;

print("distanciamento social configurado é de",distanciamentosocial,"metros")

for x in range(len(lista_loc_eixo_x)):
    cord = ("("+str(lista_loc_eixo_x[x])+","+str(lista_loc_eixo_y[x])+")")
    #print(cord)
    #print("Ponto(",lista_loc_eixo_x[x],",",lista_loc_eixo_y[x],")")
    for y in range(len(lista_loc_eixo_x)):
        distx = lista_loc_eixo_x[x]-lista_loc_eixo_x[y]
        disty = lista_loc_eixo_y[x]-lista_loc_eixo_y[y]
        disttotal = math.sqrt((distx**2)+ (disty**2))
        if not(disttotal==0):
            if disttotal <distanciamentosocial :
                #print(cord,'esbarra em', distx, disty)
                print(cord,'esbarra em', lista_loc_eixo_x[y],",",lista_loc_eixo_y[y])
                total+=1
        #print("ponto(",lista_loc_eixo_x[y],",",lista_loc_eixo_y[y],")")
print(int(total/2),"pontos ultrapassaram o distanciamento social minimo")
                   
               
    
        
