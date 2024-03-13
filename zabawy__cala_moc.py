
from math import *

li = []
def wektory(x,y,l,a,g): #x,y początek wektora , l długość wektora, a kąt o który odchylamy wektor, g kąt o który wektor jest już odchylony ( a i g w radianach)
    return (x+(l*sin(a+g)),y+(l*cos(a+g)),a+g)
def pts(n,l,x,y,a,g): #n - poziom drzewa, l długośćka galęźi, (x,y) koniec galężi(początek nastepnych dwóch),a kąt o który odchylamy wektor, g kąt o który wektor jest już odchylony ( a i g w radianach)(a powinno sięrównać -g)
    if n > 0:
        pom = wektory(x,y,l,a,g)
        pom2 = [n,a+g,(((x+pom[0])/2),(y+pom[1])/2),sqrt((abs(x-pom[0])**2)+(abs(y-pom[1])**2))]
        li.append(pom2)
        pts(n-1,l/2,pom[0],pom[1],a,pom[2])
        pts(n-1,l/2,pom[0],pom[1],-a,pom[2])
def tree(n,l,a):
    
    pts(n,l,0,0,a,-a)
    print(len(li))
