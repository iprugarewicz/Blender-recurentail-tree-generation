import bpy
def cyl(l,a,y,z,w):
    bpy.ops.mesh.primitive_cylinder_add(vertices =64,radius = w,depth= l, rotation =(a,0,0),location=(0,y,z))

import math

li = []
def wektory(x,y,l,a,g): #x,y początek wektora , l długość wektora, a kąt o który odchylamy wektor, g kąt o który wektor jest już odchylony ( a i g w radianach)
    return (x+(l*math.sin(a+g)),y+(l*math.cos(a+g)),a+g)
def pts(n,l,x,y,a,g): #n - poziom drzewa, l długośćka galęźi, (x,y) koniec galężi(początek nastepnych dwóch),a kąt o który odchylamy wektor, g kąt o który wektor jest już odchylony ( a i g w radianach)(a powinno sięrównać -g)
    if n > 0:
        pom = wektory(x,y,l,a,g)
        pom2 = [n,a+g,(((x+pom[0])/2),((y+pom[1])/2)),math.sqrt((abs(x-pom[0])**2)+(abs(y-pom[1])**2))]
        li.append(pom2)
        pts(n-1,l/1.1,pom[0],pom[1],a,pom[2])
        pts(n-1,l/1.4,pom[0],pom[1],-a,pom[2])
def tree(n,l,a,w):
    w = w/n
    pts(n,l,0,0,a,-a)
    for i in li:
        cyl(i[3],-1*i[1],i[2][0],i[2][1],w*i[0]*0.1)
        


tree(11,5,0.4,2)