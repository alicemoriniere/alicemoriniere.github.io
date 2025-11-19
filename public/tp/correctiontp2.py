import csv
import numpy as np
from math import *
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy

## Exemples

## Exemple 1

x=np.linspace(0,4*pi,100)
y=np.sin(x)
z=np.cos(x)
fig, ax=plt.subplots()
ax.plot(x,y)
ax.plot(x,z)
plt.show()

## Exemple 2

x=np.linspace(0,pi,100)
fig, axs=plt.subplots(2,2)
axs[0,0].plot(x,np.sin(x))
axs[0,1].plot(x,np.sin(2*x))
axs[1,0].plot(x, np.cos(x))
axs[1,1].plot(x,np.cos(2*x))
plt.show()

## Exemple 3

x=stats.uniform.rvs(size=(2,100))
fig, ax=plt.subplots()
ax.plot(x[0,:],x[1,:], 'o')
plt.show()

## Exemple 4

fig, ax=plt.subplots()
X=stats.expon.rvs(scale=0.5, size=10000)
ax.hist(X,bins=30, density=True, label="histogramme")
fig.suptitle("Exponentielle de paramètre 2")
x=np.arange(0,max(X), 0.01)
ax.plot(x,stats.expon.pdf(x, scale=0.5), label="densité")
ax.legend()
plt.show()

## Exemple 4 bis (plus simple selon moi):

X=stats.expon.rvs(scale=0.5, size=10000)
plt.hist(X,bins=30, density=True, label="histogramme")
x=np.arange(0,max(X), 0.01)
plt.plot(x,stats.expon.pdf(x, scale=0.5), label="densité")
plt.title("Exponentielle de paramètre 2")
plt.legend()
plt.show()

## Exemple 5

x=stats.binom.pmf(np.arange(0,21),20,0.6)
fig, ax=plt.subplots()
ax.bar(np.arange(0,21),x)
plt.show()

## Exemple 6

N=5000
p=0.7
#echantillons:
X=stats.binom.rvs(1,p, size=N)
Y1=stats.norm.rvs(loc=0, scale=1, size=N)
Y2=stats.norm.rvs(loc=4, scale=1, size=N)
Z=X*Y1 +(1-X)*Y2

def f(x):
    y=(p/sqrt(2*pi))*np.exp(-x**2/2)+((1-p)/sqrt(2*pi))*np.exp(-(x-4)**2/2)
    return y

u=np.linspace(min(Z),max(Z),200)
fig, ax=plt.subplots()
#histogramme:
ax.hist(Z,bins=100, density=True, label="histogramme")
ax.plot(u,f(u), label="densité")
fig.suptitle("Melange de deux gaussiennes")
ax.legend()
plt.show()

## Exemple 7

n=100
#un échantillon
X=stats.norm.rvs(loc=0,scale=1, size=n)
fig,ax=plt.subplots()
#on le classe:
X_sort=np.sort(X)
ax.plot(X_sort,np.arange(n)/n,drawstyle='steps-pre')
ax.plot(X_sort,stats.norm.cdf(X_sort), label='densite')
ax.legend()
plt.show()

## Exemple 8

from mpl_toolkits.mplot3d import Axes3D # jsp si c'est si essentiel que ça mais bon
fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
t = np.linspace(0, 5 * np.pi, 100)
r = np.sin(t)
x = np.cos(t)
y = t/2
ax.plot(r, x, y)
plt.show()

## Exemple 9

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
X = np.arange(-pi, pi, 0.2)
Y = np.arange(-5, 5, 0.2)
#matrices avec l'ensemble des coordonnées
#de la grille
X, Y = np.meshgrid(X, Y)
Z = X**2- Y**2
surf = ax.plot_surface(X, Y, Z, antialiased=False)
plt.show()


## Exercices

## Exercice 1

with open('C:/Users/alice/Desktop/TP_agreg/Corrections_TP/donnees2.csv', newline='') as f:
    lignes=[ligne for ligne in csv.reader(f)]

x=[eval(ligne[0]) for ligne in lignes] # on aurait pu aussi utiliser float()
y=[eval(ligne[1]) for ligne in lignes]

#plt.plot(x,y)
#plt.show()


# Ou alors on aurait pu directement travailler avec des arrays en faisant:
with open('C:/Users/alice/Desktop/TP_agreg/Corrections_TP/donnees2.csv', newline='') as f:
    lignes=np.array([np.array(ligne) for ligne in csv.reader(f)])

X=lignes[:,0].astype(float)
Y=lignes[:,1].astype(float)

plt.plot(X,Y)
plt.show()


## Exercice 2

with open('C:/Users/alice/Desktop/TP_agreg/Corrections_TP/donnees3.csv', newline='') as f:
    lignes=np.array([np.array(ligne) for ligne in csv.reader(f)])


X=lignes[:,0].astype(float)
Y=lignes[:,1].astype(float)

plt.plot(X,Y, 'v')
plt.show()


## Exercice 3

a=np.linspace(-pi, pi, 500)
b=np.linspace(-pi/2+0.01, pi/2-0.01, 500)
c=np.linspace(-1,1, 500)
d=np.linspace(-25,25, 500)

fig,ax=plt.subplots(3,2)
fig.suptitle("Toutes les fonctions trigo")
ax[0,0].plot(a,np.cos(a))
ax[0,0].set_title("cosinus")
ax[1,0].plot(a,np.sin(a))
ax[1,0].set_title("sinus")
ax[2,0].plot(b,np.tan(b))
ax[2,0].set_title("tangente")
ax[0,1].plot(c, np.arccos(c))
ax[0,1].set_title("arccosinus")
ax[1,1].plot(c, np.arcsin(c))
ax[1,1].set_title("arcsinus")
ax[2,1].plot(d, np.arctan(d))
ax[2,1].set_title("arctangente")
plt.tight_layout()
plt.show()


## Exercice 4

def binom(n):
    K=[i for i in range (n+1)]
    B=[comb(n,k) for k in K]
    plt.plot(K,B,drawstyle='steps-post')
    plt.title('Coefficients binomiaux')
    plt.show()

binom(20)


## Exercice 5

with open('C:/Users/alice/Desktop/TP_agreg/Corrections_TP/donnees4.csv', newline='') as f:
    lignes=np.array([np.array(ligne) for ligne in csv.reader(f)])

x=lignes[0,1:] # abscisses
x=np.array([eval(a) for a in x ])

y=lignes[1:,0] # ordonnées
y=np.array([eval(a) for a in y ])

z=lignes[1:,1:] # valeurs
print(np.size(z))
z=np.array([[eval(z[i,j]) for j in range (len(z[0])) ] for i in range (len(z))])

# on aurait pu faire "lignes=lignes.astype(np.float64)" pour faire tout d'un coup

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
x,y=np.meshgrid(x,y)
surf=ax.plot_surface(x,y,z)

plt.show()


## Exercice 6

def illustration_TCL(N,n): # N est le nombre d'échantillons, et n est leur taille
    M=stats.expon.rvs(scale=1,size=(N,n))
    L=(np.sum(M,axis=1)-n)/(sqrt(n))
    X=np.linspace(min(L),max(L),500)
    Y=stats.norm.pdf(X)
    plt.hist(L,20,density=True,label='histogramme échantillon')
    plt.plot(X,Y,label='densité loi normale')
    plt.title('Illustration TCL')
    plt.legend()
    plt.show()

illustration_TCL(500,1000)


## Exercice 7

def markov_avec_P(n,P,x0):
    X=np.zeros(n,dtype=int) #on indique que X contiendra seulement des entiers.
    X[0]=x0
    for k in range(n-1):
        X[k+1]=np.random.choice(a=range(len(P)), p=P[X[k],:])
        # Les états sont numérotés de 0 à len(P)-1
    return X

P=np.array([[1/3, 1/3, 1/6, 1/6], [0, 1/2, 0, 1/2], [1/4, 1/4, 1/4, 1/4], [1/3, 1/3, 1/3, 0]])
# On aurait pu le faire de façon smart mais ça m'a pris moins de temps de l'écrire comme ça que de réfléchir

X=markov_avec_P(10000,P,0)
#print(X)

# Il existe plusieurs façons de déterminer numériquement la proba invariante d'une chaîne de Markov, on reverra ça dans le TP correspondant, mais ici puisque l'on a une simulation de la chaîne, le plus simple c'est d'utiliser la fréquence empirique d'occupation (et puis selon moi c'est la méthode la plus naturelle)

mu=np.zeros(4)
for i in range(4):
    mu[i]=np.mean(X==i)

print(mu)


## Exercice 8

def simulation1():
    return(np.random.choice(a=range(4), p=[0.1,0.3,0.2,0.4]))

simulation1()

p=np.array([0.1,0.3,0.2,0.4])

def simulation2(p): # simule une variable de vecteur de proba p grâce à l'inversion de la FDR
    cdf=np.cumsum(p) # fonction de répartition
    u=np.random.random() # uniforme entre 0 et 1
    i=0
    while u>cdf[i]: # on utilise la définition de l'inverse généralisée
        i+=1
    return i

simulation2(p)


## Exercice 9

#Question 1 (on utilise la fonction de l'exo précédent)

p_bern=np.array([1/2,1/2])
B=simulation2(p_bern)
print(B)

R=2*simulation2(p_bern)-1 # pour fabriquer une Rademacher à partir d'une Bernoulli
print(R)

#Question 2 (encore une fois)

p_unif=np.ones(4)/4
U=simulation2(p_unif)
print(U)

#Question 3 (cette fois l'inverse généralisée est continue, on change de méthode)

def simulation_exp(l):
    mu=1/l
    u=np.random.random()
    return(-mu*np.log(u))

print(simulation_exp(2))

def illustration_lgn(l,n): # ATTENTION, la convergence PS s'illustre trajectoire par trajectoire !
    T=[simulation_exp(l) for i in range (n)]
    E=[]
    N=[i for i in range (1,n+1)]
    L=[l for i in N]
    for i in N:
        Ti=T[:i]
        estim=len(Ti)/np.sum(Ti)
        E.append(estim)
    plt.xlabel('N')
    plt.plot(N[50:],E[50:],label='estimation')
    plt.plot(N[50:],L[50:],label='valeur théorique')
    plt.title('Illustration de la convergence P.S.')
    plt.legend()
    plt.show()

illustration_lgn(2,5000)

# On aurait pu tout faire d'un coup en faisant U=np.random.random(size=n) puis X=-mu*np.log(U)


## Exercice 10

def densite(x):
    return ((pi/2)*np.sin(pi*x))

def rejet():
    b=False
    while b==False:
        X=stats.uniform.rvs()
        Y=stats.uniform.rvs(loc=0,scale=2)
        if densite(X)>Y:
            b=True
    return(X)

def illustration(n): #pour vérifier que ça marche bien, on trace un histogramme
    E=[rejet() for i in range (n)]
    plt.hist(E, 25, density=True,label='Histogramme données simulées')
    T=np.linspace(min(E),max(E),100)
    plt.plot(T,densite(T),label='Densité souhaitée')
    plt.legend()
    plt.show()

illustration(2000)


## Exercice 11

#Question 1
#calculer E[\phi(\epsilon Z)]

#Question 2

def g(x):
    return ((1/2)*np.exp(-abs(x)))

def f(x):
    return((np.exp(-(x**2)/2))/sqrt(2*pi))

def rejet_gaussienne():
    C=sqrt(2*np.exp(1)/pi)
    b=False
    while b==False:
        R=2*simulation2(p_bern)-1 # Rademacher
        E=stats.expon.rvs(scale=1) # exponentielle
        X=R*E # variable de densité g
        U=stats.uniform.rvs()
        if f(X)>C*g(X)*U:
            b=True
    return(X)

#Question 3

def illustration_gaussienne(n):
    E=[rejet_gaussienne() for i in range (n)]
    plt.hist(E, 25, density=True, label='Histogramme données simulées')
    T=np.linspace(min(E),max(E),100)
    plt.plot(T,f(T),label='Densité souhaitée')
    plt.legend()
    plt.show()

illustration_gaussienne(2000)


##Exercice 12

def simulation_pareto():
    u=np.random.random()
    return (u**(-1/2))

def moyenne_empirique(n,c): # n est la taille de l'échantillon, c la constante que l'on se fixe
    E=np.array([simulation_pareto() for i in range(n)])
    E_cond=E[E>=c]
    return(np.mean(E_cond))

C=np.linspace(1,5,200)
M=[moyenne_empirique(10000,c) for c in C]
plt.plot(C,M,label='Espérance conditionnelle empirique')
plt.plot(C,2*C,label="2 fois l'identité")
plt.legend()
plt.show()
#le résultat est de plus en plus erratique au fur et à mesure que c grandit, sûrement parce que l'on a de moins en moins de valeurs


## Exercice 13

a=1
alpha=1

def fdr_frechet(x):
    return(np.exp(-(a/x)**alpha))

def fdr_frechet_inv(y):
    return(a*(-np.log(y))**(-1/alpha))

def simulation_frechet():
    u=np.random.random()
    return(fdr_frechet_inv(u))

def illustration_fdr(n): # n est la taille de l'échantillon
    E=[simulation_frechet() for i in range(n)]
    E=np.sort(E)
    F_emp=np.arange(n)/n
    plt.plot(E,F_emp,drawstyle='steps-pre',label='Fonction de répartition empirique')
    X = np.linspace(min(E),max(E),500)
    F_th=[fdr_frechet(x) for x in X]
    plt.plot(X,F_th,label='Fonction de répartition théorique')
    plt.legend()
    plt.show()

illustration_fdr(100)


## Exercice 14

def variation_totale(n,l):
    v=0
    for k in range(n+1):
        v+=abs(stats.poisson.pmf(k,mu=l)-stats.binom.pmf(k,n,l/n))
    v+=1-stats.poisson.cdf(n,mu=l)
    return(v)

def representation_vt(N,l): #on représente la variation totale des 2 lois en fonction de n, pour n entre 1 et N
    N=np.arange(1,N+1)
    V=[variation_totale(n,l) for n in N]
    plt.plot(N,V)
    plt.title('Variance totale entre les deux lois en fonction de n')
    plt.xlabel('n')
    plt.ylabel('variation totale')
    plt.show()

representation_vt(100,2)

def representation_loi(n,l): #représentation des deux lois pour n fixé
    N=np.arange(0,n+1)
    B=stats.binom.pmf(N,n,l/n)
    P=stats.poisson.pmf(N, mu=l)
    fig,axs=plt.subplots(2,2)
    axs[0,0].bar(N,B, 0.3, color='b', label='loi binomiale')
    axs[0,0].bar(N,P, alpha=0.3, color='r', label='loi de Poisson')
    axs[1,0].bar(N,B, color='b')
    axs[1,1].bar(N,P, color='r')
    fig.legend()
    plt.show()

representation_loi(10,2)


## Exercice 15

def proba(n,N): #estimation de p(n) avec un échantillon de taille N
    D=np.zeros(N)
    for i in range(N):
        A=2*stats.binom.rvs(1, 0.5, size=(n,n))-1 # matrice de taille n de Rademacher
        D[i]=np.linalg.det(A)
    p=np.mean(D==0)
    return (p)

def illustration_proba_det(n,N): # tracé de l'esimation de p(k) pour k entre 1 et n, avec pour chaque calcul des échantillons de taille N
    T=np.arange(1,n+1)
    P=[proba(k,N) for k in T]
    plt.plot(T,P)
    plt.title('Estimation de p(n) en fonction de n')
    plt.xlabel('n')
    plt.ylabel('estimation de p(n)')
    plt.show()

illustration_proba_det(50,100)

def esperance(n,N): #estimation de l'espérance demandée pour une matrice de taille n, avec un échantillon de taille N
    D=np.zeros(N)
    for i in range(N):
        A=2*stats.binom.rvs(1, 0.5, size=(n,n))-1 # matrice de taille n de Rademacher
        D[i]=np.linalg.det(A)**2
    e=np.mean(D)
    return (e)

def illustration_esperance(n,N): # tracé de l'espérance empirique pour k entre 1 et n, avec pour chaque calcul des échantillons de taille N
    T=np.arange(1,n+1)
    P=[esperance(k,N) for k in T]
    plt.plot(T,P)
    plt.title('Espérance empirique en fonction de n')
    plt.xlabel('n')
    plt.show()

illustration_esperance(3,1000)
