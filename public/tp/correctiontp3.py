import numpy as np
from math import *
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy

## Exercice 1

def f(x):
    return(4*np.sqrt(1-x**2))

f=np.vectorize(f)

def approximation_integrale_1(n):
    X=stats.uniform.rvs(loc=0,scale=1,size=n)
    S=np.mean(f(X))
    return(S)

print(approximation_integrale_1(5000))

def g(x):
    u=(x[0]**2+2*x[1]**2+3*x[2]**2 <= 1)
    return(u)


def approximation_integrale_2(n):
    X=stats.uniform.rvs(loc=-1,scale=2,size=(n,3))
    S=np.mean(np.array([g(X[i]) for i in range (len(X))]))
    return((2**3)*S) #on n'oublie pas la renormalisation par la taille du pavé !

print(approximation_integrale_2(5000))


## Exercice 2

def h(X):
    u=(np.linalg.norm(X)**2<=1)
    return(u)


def boule(n,d):
    X= stats.uniform.rvs(loc=-1,scale=2,size=(n,d))
    S=np.mean([h(x)for x in X])
    return((2**d)*S) # encore une fois, on n'oublie pas la renormalisation !

print(boule(5000,2))

def ecart_avec_la_théorie(n,d):
    a=np.pi**(d/2)
    b=scipy.special.gamma((d/2)+1)
    E= abs(boule(n,d)-(a/b))
    return(E)

print(ecart_avec_la_théorie(5000,2))
print(ecart_avec_la_théorie(5000,4))


## Exercice 3

# Question 1 (J'ai fait toutes les questions séparées, mais il vaut mieux direct faire la question 3)

def i(x):
    return(sqrt(np.pi)*np.cosh(x))


def approximation_integrale_3(n):
    X= stats.norm.rvs(loc=0,scale=(1/sqrt(2)),size=n)
    S=np.mean(i(X))
    return(S)

print(approximation_integrale_3(5000))

# Question 2

# ATTENTION, les questions sont un peu mal posées, mais il faut le MEME ALEA pour l'estimateur de l'intégrale et pour l'estimateur de la variance (et plus tard pour les bornes de l'intervalle). On va donc refaire un programme à chaque fois

def appproximation_int_et_variance(n):
    X=stats.norm.rvs(loc=0,scale=(1/sqrt(2)),size=n)
    S=np.mean(i(X))
    sigma= np.mean((i(X)-S)**2)
    return((S,sigma))

print(appproximation_int_et_variance(5000))

# Question 3

# ATTENTION, de nouveau, il faut tout refaire, parce qu'il faut le même aléa pour toutes les quantités calculées !! (il faut de nouveau le même aléa à n fixé pour I_n, \sigma_n et les bornes, mais aussi pour tous les n, on regarde une seule et même trajectoire !!)

def estim_et_intervalle(N):
    S=[] #contient les estimateurs
    I1=[] #contient les bornes inf
    I2=[] #contient les bornes sup
    T=np.arange(1,N+1)
    X=stats.norm.rvs(loc=0,scale=(1/sqrt(2)),size=N)
    Y=i(X)
    for n in range(1,N+1):
        Yn=Y[:n]
        s=np.mean(Yn)
        sigma=sqrt(np.mean((Yn-s)**2))
        c=1.96*sigma/sqrt(n)
        i1=s-c
        i2=s+c
        S.append(s)
        I1.append(i1)
        I2.append(i2)
    plt.plot(T[15:],S[15:],label='estimateur intégrale') # je commence à 15 pour éviter les pics abberants des premières valeurs
    plt.plot(T[15:],I1[15:],label='borne inf')
    plt.plot(T[15:],I2[15:],label='borne sup')
    plt.plot(T[15:],2.273*np.ones(len(T[15:])), label='valeur théorique')
    plt.legend()
    plt.show()

estim_et_intervalle(10000)


## Exercice 4

def l(x):
    u=np.exp(x)-1
    return(np.maximum(0,u)) # j'ai eu des problèmes bizarres avec max())

l=np.vectorize(l)

def m(x):
    u=sqrt(2*x)
    a=np.exp(u)-1
    return((1/sqrt(2*pi))*a/u)

m=np.vectorize(m)

def approximation_integrale_4(n):
    X=stats.norm.rvs(loc=0,scale=1,size=n)
    S=np.mean(l(X))
    V=np.mean((l(X)-S)**2)
    return(S,V)

print(approximation_integrale_4(10000))

def approximation_integrale_5(n):
    Y=stats.expon.rvs(scale=1,size=n)
    S=np.mean(m(Y))
    V=np.mean((m(Y)-S)**2)
    return(S,V)

print(approximation_integrale_5(10000)) # variance BEAUCOUP plus petite !


## Exercice 5

def p(x):
    u=1-np.exp(x)
    return(np.maximum(0,u))

p=np.vectorize(p)

def approximation_integrale_6(n):
    X=stats.norm.rvs(loc=0,scale=1,size=n)
    S=np.mean(p(X))
    V=np.mean((p(X)-S)**2)
    return(S+np.exp(1/2)-1,V)

approximation_integrale_6(10000) # variance encore plus petite que la précédente !


## Exercice 6

def approximation_integrale_7(n):
    X=stats.norm.rvs(loc=0,scale=1,size=n)
    Y=(l(X)+l(-X))/2
    S=np.mean(Y)
    V=np.mean((Y-S)**2)
    return(S,V)

approximation_integrale_7(1000) # là c'est moins bien que précédemment...

# Classement final : (en terme de variance, donc plus petit = meilleur )
# méthode naïve > symétrisation > échantillonage préférentiel > variable de contrôle