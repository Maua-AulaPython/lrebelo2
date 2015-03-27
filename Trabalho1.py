# -*- coding: cp1252 -*-\
from math import sqrt
from math import atan2
from math import atan
from math import degrees
from math import sin
from math import cos
def dist(a,b):
    if (len(a)==2 & len(b)==2):
        return sqrt((float(a[0])-float(b[0]))**2 + (float(a[1])-float(b[1]))**2)
    else:
        print "pontos não completos"
        return -1



def maior_dist(L):
    i=0
    j=i+1
    b=-1
    while i<len(L)-1:
        if(j<len(L)):
            a=dist(L[i],L[j])
            j+=1
            if ((a > b) | (b==-1)):
                b=a;
        else:
            i+=1
            j=i+1
    return b

   
def coord_polar (P):
    r= sqrt(float(P[0])**2 + float(P[1])**2)
    tt=atan2(P[1],P[0])
    R=(r,degrees(tt))
    return R

def tri_ret(A,B,C):
    if ((A**2+B**2)==C**2):
        ar=(A*B)/2.0
        print "O triangulo é retangulo e sua área é:%f" %ar
    else:
        print "os valores lidos (%d,%d,%d) não formam um triangulo retangulo" % (A,B,C)

def GPS(x,y,z):
    l=atan(y/x)
    h=0
    N=1
    pd=1
    P=sqrt(float(x)**2+float(y)**2)
    E=0.00669454185
    a=6378160
    for i in range(5):
        pd=((z/P)*(1/(1-E*(N/(N+h)))))
        t=atan(pd)
        N=a/sqrt(1-E*(sin(t)**2))
        h=(P/cos(t))-N
    return (degrees(t),degrees(l),h)
            
           
# teste das funcoes
P1=(1,2)
P2=(2,1)
print "distancia entre pontos: %f" %dist(P1,P2)
L=[(1,2), (2,3), (4,5), (0,0),(1,-2.3),(-1,-0.5)]
print "maior distancia da lista:%f"%maior_dist(L)
P=(-32,45)
print "coordenada polar:%s" %(coord_polar(P),)
tri_ret(6,8,10)
(x,y,z)=(4010210.546,-4260166.288,-2533008.133)
print"coordenadas GPS: %s"%(GPS(x,y,z),)


