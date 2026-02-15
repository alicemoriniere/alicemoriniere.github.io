import numpy as np
from math import *
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy
import csv


## Exercice 1

def test_chi_2(A,p0,X,alpha): # on précise aussi A pour se simplifier la vie
    n=len(X)
    p_min=min(p0)
    if n*p_min < 5:
        print("Regrouper les classes svp") # pour satisfaire la condition d'approximation
    F=[np.sum(X==i) for i in A]
    D,p_value=scipy.stats.chisquare(F,p0*n)
    s=stats.chi2.ppf(q=1-alpha, df=len(A)-1)
    if D>s:
        print("On rejette H0")
    else:
        print("On ne rejette pas H0")

def test_chi_2_bis(A,p0,X,alpha): # on peut aussi travailler avec la p valeur
    n=len(X)
    p_min=min(p0)
    if n*p_min < 5:
        print("Regrouper les classes svp") # pour satisfaire la condition d'approximation
    F=[np.sum(X==i) for i in A]
    D,p_value=scipy.stats.chisquare(F,p0*n)
    print(p_value)
    if p_value<=alpha:
        print("On rejette H0")
    else:
        print("On ne rejette pas H0")


## Exercice 2

X=stats.randint.rvs(low=0, high=10, size=200)
A=np.arange(0,10)
alpha=0.01
p0=np.ones(10)/10
test_chi_2(A,p0,X,alpha) # quelle surprise, on ne rejette pas !

test_chi_2_bis(A,p0,X,alpha) # là non plus !


## Exercice 3

n=200
alpha=0.05
# On écrit les données mais peut être qu'il va falloir les regrouper
A0=np.arange(0,12)
f0=np.array([6,15,40,42,37,30,10,9,5,3,2,1])


theta=np.sum(A0*f0)/n # estimateur du maximum de vraisemblance
print(theta)
p0=stats.poisson.pmf(A0, mu=theta)
print(n*p0)
# On laisse telle quelle la première qui est quasiment à 5, mai son va regrouper à partir de la 8ème.

A=np.arange(0,9)
f=np.array(list(f0[:8])+[np.sum(f0[8:])])
p=stats.poisson.pmf(A, mu=theta)
p[-1]=1-stats.poisson.cdf(7,mu=theta) # il faut que p se somme à 1, il doit être un vecteur de proba

D,p_value=stats.chisquare(f,p*n)
t= stats.chi2.ppf(q=1-alpha, df=len(A)-1-1)
if D>t:
    print ("On rejette H0")
else:
    print("On ne rejette pas H0")
# On ne rejette pas H0

# De nouveau, on peut aussi utiliser la p-valeur :
print(p_value)
if p_value<=alpha:
    print ("On rejette H0")
else :
    print("On ne rejette pas H0")


## Exercice 4

# Dans l'exemple, on nous donne directement la matrice des occurrences, que l'on prend ici en entrée.
def test_ind_chi_2(F,alpha):
    r,s=len(F),len(F[0])
    D, p_valeur, dlib, expected=stats.chi2_contingency(F)
    s=stats.chi2.ppf(q=1-alpha,df=(r-1)*(s-1))
    if D>s:
        print ("On rejette H0")
    else:
        print("On ne rejette pas H0")

# De nouveau, on peut faire le test en utilisant la p value.
def test_ind_chi_2_bis(F,alpha):
    r,s=len(F),len(F[0])
    D, p_valeur, dlib, expected=stats.chi2_contingency(F)
    print(p_valeur)
    if p_valeur<=alpha:
        print("On rejette H0")
    else:
        print("On ne rejette pas H0")

# Si la matrice des occurences n'est pas fournie, on utilise la fonction suivante.

def matrice_frequences(V,r,s):
    n=len(L)
    F=np.zeros((r,s))
    for i in range(n):
        (x,y)=V[i]
        F[x,y]+=1
    return(F)

# Test
L=stats.randint.rvs(low=0,high=4,size=(25,2))
F=matrice_frequences(L,4,4)
test_ind_chi_2(F,0.005)
test_ind_chi_2_bis(F,0.005)


## Exercice 5

F_nat=np.array([[2331536,663540],[715085,135493]])
test_ind_chi_2(F_nat,0.001)
test_ind_chi_2_bis(F_nat,0.001)

# On rejette très fort.


## Exercice 5 bis (exemple de test d'homogénéité)

alpha=0.05
E1= stats.randint.rvs(low=0, high=10, size=200)
E2= stats.randint.rvs(low=0, high=10, size=200)
E3= stats.randint.rvs(low=0, high=10, size=200)

D,p_value=scipy.stats.friedmanchisquare(E1,E2,E3)
print(p_value)
if p_value<alpha:
    print("On rejette H0")
else:
    print("On ne rejette pas H0")

# sans surprise, on ne rejette pas !


## Exercice 6

## Question 1

Ech=scipy.stats.norm.rvs(size=1000)
X=np.linspace(min(Ech),max(Ech),200)
F_th=scipy.stats.norm.cdf(X)

Ech1=np.sort(np.copy(Ech[:50]))
Ech2=np.sort(np.copy(Ech[:100]))
Ech3=np.sort(np.copy(Ech[:500]))
Ech4=np.sort(np.copy(Ech))


plt.plot(Ech1,np.arange(len(Ech1))/len(Ech1),drawstyle='steps-post',label='50 données')
plt.plot(Ech2,np.arange(len(Ech2))/len(Ech2),drawstyle='steps-post',label='100 données')
plt.plot(Ech3,np.arange(len(Ech3))/len(Ech3),drawstyle='steps-post',label='500 données')
plt.plot(Ech4,np.arange(len(Ech4))/len(Ech4),drawstyle='steps-post',label='1000 données')
plt.plot(X,F_th,label='fonction de répartition théorique')
plt.legend()
plt.show()

## Question 2

# cf récap

## Question 3

## Glivenko-Cantelli

def calcul_norme_inf_normale(X):
    X_tri=np.sort(X)
    E=[]
    n=len(X)
    F_th=stats.norm.cdf(X_tri)
    F1=np.arange(0,n)/n
    F2=np.arange(1,n+1)/n
    e1=np.max(np.abs(F_th-F1))
    e2=np.max(np.abs(F_th-F2))
    return(max(e1,e2))


def illustration_gc(N): # trace ||F_n-F|| en fonction de n (jusqu'à N)
    X=stats.norm.rvs(loc=0,scale=1,size=N)
    D=[]
    for n in range (10,N+1):
        Xn=X[:n]
        D.append(calcul_norme_inf_normale(Xn))
    plt.plot(np.arange(10,N+1),D, label='Distance infinie')
    plt.title('Illustration du théorème de Glivenko-Cantelli pour des variables normales')
    plt.show()

illustration_gc(1000)

## Kolmogorov-Smirnov

def fonction_rep_th(x,M): # M est un seuil de précision pour le calcul de la série
    s=0
    for k in range(1,M+1):
        s+=((-1)**(k-1))*exp(-2*(k*x)**2)
    return(1-2*s)


def illustration_ks(n,N,M): # illustre la convergence en loi grâce à la convergence des fonctions de rep
    # on crée un N échantillon de || F_n - F ||, où chacune de ces normes est calculée à partir d'un n échantillon de variables (en l'occurence normales), puis on trace la fonction de répartirion empirique de cet échantillon de norme, que l'on compare avec la fonction de répartition de la loi de Kolmogorov
    D=[]
    for _ in range (N):
        X=stats.norm.rvs(loc=0,scale=1, size=n)
        d=calcul_norme_inf_normale(X)
        D.append(np.sqrt(n)*d)
    T=np.linspace(min(D),max(D),250)
    F_th=[fonction_rep_th(x,M) for x in T]
    plt.plot(T,F_th,label='Fonction de répartition théorique')
    plt.plot(np.sort(D),np.arange(N)/N,drawstyle='steps-post',label='Fonction de répartition empirique')
    plt.title('Illustration du théorème de Kolmogorov-Smirnov pour des variables normales')
    plt.show()

illustration_ks(5000,500,20)


## Exercice 7

alpha=0.05

with open('C:/Users/alice/Desktop/TP_agreg/Corrections_TP/donnees5.csv', newline='') as f:
    lignes=np.array([ligne for ligne in csv.reader(f)])

Y=lignes[:,0].astype(np.float64)
D, p_valeur=stats.kstest(Y, stats.expon.cdf)
print(p_valeur)
if p_valeur<=alpha:
    print("On rejette H0")
else:
    print("On ne rejette pas H0")

# En fait, on remarque (merci Samuel), que l'échantillon suit une loi exponentielle, mais translaté de 1 :
Z=Y-1
D,p_valeur=stats.kstest(Z, stats.expon.cdf)
print(p_valeur)
if p_valeur<=alpha:
    print("On rejette H0")
else:
    print("On ne rejette pas H0")

## Exercice 7 bis (exemple de test d'homogénéité)

alpha=0.05
E1=stats.expon.rvs(scale=1, size=200)
E2=stats.expon.rvs(scale=1, size=200)

D,p_value=scipy.stats.ks_2samp(E1,E2)
print(p_value)
if p_value<=alpha:
    print("On rejette H0")
else:
    print("On ne rejette pas H0")

# sans surprise, on ne rejette pas !