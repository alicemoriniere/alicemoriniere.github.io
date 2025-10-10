import csv
import numpy as np
from math import *
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy


## Exercice 1

with open('C:/Users/alice/Desktop/TP_agreg/Corrections_TP/donnees.csv', newline='') as f:
    lignes=[ligne for ligne in csv.reader(f)]  # attention c'est une  liste de chaines de caracteres

x=lignes[0]
y=lignes[1]
plt.plot([eval(a) for a in x[1:]],[ eval(u) for u in y[1:]])
plt.show()


## Exercice 2

#Si x était un array (ce qui n'est pas la consigne !):
x=stats.randint.rvs(low=0, high=9, size=50)
a=np.sum(x==1) #compte le nombre de 1
i=np.where(x==2)[0][0] #premier indice de la valeur 2
#Mais on ne peut pas ajouter d'élément dans un array, donc on suit la consigne et on utilise une liste
print(x)

x=list(x)
a=x.count(1) #compte le nombre de 1
i=x.index(2) #premier indice de la valeur 2
x.insert(i,'ici')


## Exercice 3

M=np.array([[(i-j) for j in range (1,5)] for i in range(1,4)])

print(M) #la matrice
print(M[0,:]) #sa première ligne
print(M[:2,:]) #ses deux premières lignes
print(M[:,0]) #sa première colonne
print(M[:,-1]) #sa dernière colonne
print(M[-1,-1]) #l'élement en bas à droite
print(M[:2,2:]) #la sous matrice demandée


## Exercice 4

v=stats.randint.rvs(low=0,high=51,size=1000)
print(v)
w=[]
for i in range (len(v)):
    if v[i]%2==0 or v[i]%5==0:
        w.append(v[i])
w=np.array(w)
print(w)

# OU plus rapidement

x=v[(v%2==0)|(v%5==0)]
print(x)


## Exercice 5

x=stats.norm.rvs(size=10)
print(x)
y=x[::-1] # vecteur dans l'ordre inverse
print(y)


## Exercice 6

x=np.array([(-1)**i for i in range(10)])
print(x)
# OU directement avec un array :
y=(-1)**np.arange(10)
print(y)


## Exercice 7

#Première matrice:
A=2*np.eye(3)
A[0,-1],A[-1,0]=1,1
print(A)

#Deuxième matrice:
B=np.ones((3,3)) #faire attention à mettre le couple dimension entre ()
B[1,0], B[1,-1]=2,2
print(B)

#Troisième matrice:
C=np.ones((3,3)) #faire attention à mettre le couple dimension entre ()
C[1,1], C[-1,-1]=2,3
print(C)


## Exercice 8

#Question 1
A=np.diag([i for i in range (1,7)])
print(A)

#Question 2
B=np.arange(1,37).reshape(6,6)
print(B)

#Question 3
C=np.arange(1,7)*np.ones((6,6))
print(C)

#Question 4
D1=2*np.ones((2,2))
D2=np.arange(1,17).reshape((4,4))
D=scipy.linalg.block_diag(D1,D2)
print(D)

#Question 5
E=np.array([(-1)**(i+j) for i in range(1,7) for j in range(1,7)]).reshape(6,6)
print(E)

#OU

F=np.array([[(-1)**(i+j) for j in range(1,7)] for i in range(1,7) ])
print(F)

#Question 6
G=np.eye(6)
for i in range(1,6):
    G=G+(i+1)*np.diag(np.ones(6-i),i) + (i+1)*np.diag(np.ones(6-i),-i)
print(G)


## Exercice 9

M=np.arange(1,145).reshape(12,12)
print(M)

#Question 1
print(M[:7,6:])

#Question 2
print(M[::2,::2]) ##il suffit de prendre un coefficient sur deux

#Question 3
print(M[(1,2,5,6,9,10),(1,2,5,6,9,10)])


## Exercice 10

def diff(v):
    V=[v[0]]
    for j in range(1,len(v)):
        V.append(v[j]-v[j-1])
    return np.array(V)

V=np.arange(1,10)
v=np.cumsum(V)
print(diff(v))


## Exercice 11

def zorro(n):
    Z=np.zeros((n,n))
    Z[0,:]=np.ones(n)
    Z[-1,:]=np.ones(n)
    a=np.arange(n)[::-1]
    Z[a, range(n)]=1
    return(Z)


## Exercice 12

# le triangle ABC est défini comme l'intersection des trois demi-plans:
# - le demi-plan de bord (AB) contenant C
# - le demi-plan de bord (AC) contenant B
# - le demi-plan de bord (BC) contenant A

def triangle(A,B,C,M):
    vAB=B-A
    vAC=C-A
    vBC=C-B
    vAM=M-A
    vBM=M-B
    vCM=M-C
    c1= ((-vAB[1]*vAM[0]+vAB[0]*vAM[1]))*((-vAB[1]*vAC[0]+vAB[0]*vAC[1]))
    c2= ((-vAC[1]*vAM[0]+vAC[0]*vAM[1]))*((-vAC[1]*vAB[0]+vAC[0]*vAB[1]))
    c3= ((-vBC[1]*vBM[0]+vBC[0]*vBM[1]))*((vBC[1]*vAB[0]-vBC[0]*vAB[1]))
    if (c1>=0) and (c2>=0) and (c3>=0):
        return True
    else:
        return False

A=np.array([-2,1.5])
B=np.array([3,5])
C=np.array([3.6,-2.7])
M1=np.array([1.4,1.8])
M2=np.array([-2,-2])
M3=np.array([6,3])
M4=np.array([3,-1])

print(triangle(A,B,C,M1))
print(triangle(A,B,C,M2))
print(triangle(A,B,C,M3))
print(triangle(A,B,C,M4))


## Exercice 13

def Pascal(n):
    P=np.diag(np.ones(n))
    P[:,0]=np.ones(n)
    for i in range(2,n):
        for j in range(1,i):
            P[i,j]=P[i-1,j-1]+P[i-1,j]
    return(P)

print(Pascal(10))


## Exercice 14

def Eratosthene(n):
    E= [0,0]+[i for i in range(2, n+1)] #1 n'est pas un nombre premier donc on l'enlève, mais on ajoute les deux zéros pour faciliter les choses côté indices
    for i in range(2, n+1):
        if E[i]!=0:
            # c'est un nombre 1er: on garde, mais on enleve ses multiples
            for j in range(2*i, n+1, i):
                E[j] = 0
    return [p for p in E if p!=0]

print(Eratosthene(100))

def comptage_premier(x):
    return (len(Eratosthene(floor(x))))

X=np.linspace(0,100,500)
Y=[comptage_premier(x) for x in X]
plt.plot(X,Y)
plt.show()


## Exercice 15

def Vandermonde(v):
    V=np.array([v**i for i in range (0,len(v))])
    return(V,np.linalg.det(V))

print(Vandermonde(np.arange(1,7)))


##Exercice 16 (correction de Nathalie)
import turtle

def von_koch(longueur,n):
    " applique n fois l'algo à un segment de longueur n"
    if n==1:
        turtle.forward(longueur) #Move the turtle forward by the specified distance.
    else:
        d=longueur/3.
        von_koch(d,n-1)
        turtle.left(60)# tourne à gauche de 60 degres
        von_koch(d,n-1)
        turtle.right(120)
        von_koch(d,n-1)
        turtle.left(60)
        von_koch(d,n-1)

def flocon(longueur,n):
    turtle.up()#relever le crayon
    turtle.goto(-longueur/2., longueur/3.) # on se place en haut à gauche
    turtle.down() #on abaisse le crayon
    for i in range(3):
        von_koch(longueur,n)
        turtle.right(120)

def von_koch_random(longueur,n):
    " applique n fois l'algo à un segment de longueur n"
    if n==1:
        turtle.forward(longueur) #Move the turtle forward by the specified distance.
    else:
        d=longueur/3.
        von_koch_random(d,n-1)
        X=stats.binom.rvs(1,0.5)
        if X==1:
            turtle.left(60)# tourne à gauche de 60 degres
            von_koch_random(d,n-1)
            turtle.right(120)
            von_koch_random(d,n-1)
            turtle.left(60)
        else:
            turtle.forward(d)
        von_koch_random(d,n-1)

def flocon_random(longueur,n):
    turtle.up()#relever le crayon
    turtle.goto(-longueur/2., longueur/3.) # on se place en haut à gauche
    turtle.down() #on abaisse le crayon
    for i in range(3):
        von_koch_random(longueur,n)
        turtle.right(120)


def flocon_alea(longueur,n): # ca fait par tiers de dessin
    turtle.up()#relever le crayon
    turtle.goto(-longueur/2., longueur/3.) # on se place en haut à gauche
    for i in range(3):
        X=stats.binom.rvs(1,0.5)
        if X==1:
            turtle.down() #on abaisse le crayon
        else:
            turtle.up()
        von_koch(longueur,n)
        turtle.right(120)

def von_koch_alea(longueur,n):
    " applique n fois l'algo à un segment de longueur n"
    if n==1:
        X=stats.binom.rvs(1,0.5)
        if X==0:
            turtle.up()
        else:
            turtle.down()
        turtle.forward(longueur) #Move the turtle forward by the specified distance.
        #turtle.down()
    else:
        d=longueur/3.
        von_koch_alea(d,n-1)
        turtle.left(60)# tourne à gauche de 60 degré
        von_koch_alea(d,n-1)
        turtle.right(120)
        von_koch_alea(d,n-1)
        turtle.left(60)
        von_koch_alea(d,n-1)

def flocon2(longueur,n):
    turtle.up()#relever le crayon
    turtle.goto(-longueur/2., longueur/3.) # on se place en haut à gauche
    for i in range(3):
        von_koch_alea(longueur,n)
        turtle.right(120)
