import csv
import numpy as np
from math import *
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy


## Exercice 1

## Question 1

# $\frac{n}{S_n} \xrightarrow[n \to \infty]{\text{p.s.}} \lambda $

## Question 2

def illustration_cv_ps(l,n): # ATTENTION, la convergence PS s'illustre trajectoire par trajectoire !!!
    T=stats.expon.rvs(scale=1/l, size=n)
    E=[]
    N=np.arange(50,n+1) # Je commence à 50 pour ne pas avoir trop des pics abberants aux premières valeurs qui écrasent tout le graphique
    L=[l for i in N]
    for i in N:
        Ti=T[:i]
        estim=len(Ti)/np.sum(Ti)
        E.append(estim)
    plt.xlabel('N')
    plt.plot(N,E,label='estimation')
    plt.plot(N,L,label='valeur théorique')
    plt.title('Illustration de la convergence P.S.')
    plt.legend()
    plt.show()

illustration_cv_ps(2,10000)


## Exercice 2

## Question 1

# $\frac{\lambda S_n - n}{ \sqrt{n} } \xrightarrow[n \to \infty]{\mathcal L } \mathcal N (0,1) $

## Question 2

def illustration_cv_loi_fdr_exp(l,n,N):
    M=stats.expon.rvs(scale=1/l,size=(N,n))
    E=np.array([((l*sum(M[i])-n)/sqrt(n)) for i in range (N)])
    E=np.sort(E)
    F_emp=np.arange(N)/N
    plt.plot(E,F_emp,drawstyle='steps-pre',label='Fonction de répartition empirique')

    X = np.linspace(min(E),max(E),500)
    F_th=stats.norm.cdf(X,loc=0,scale=1)
    plt.plot(X,F_th,label='Fonction de répartition théorique')

    plt.title('Illustration de la convergence en loi via les fonctions de répartition')
    plt.legend()
    plt.show()

illustration_cv_loi_fdr_exp(2,500,100)

## Question 3

def illustration_cv_loi_hist_exp(l,n,N): # n est la taille des échantillons, et N le nombre des échantillons
    M=stats.expon.rvs(scale=1/l,size=(N,n))
    L=np.array([((l*sum(M[i])-n)/sqrt(n)) for i in range (N)])
    X=np.linspace(min(L),max(L),200)
    Y=stats.norm.pdf(X)
    plt.hist(L,25,density='True', label='histogramme échantillon')
    plt.plot(X,Y,label='densité loi normale')
    plt.title('Illustration TCL')
    plt.legend()
    plt.show()

illustration_cv_loi_hist_exp(2,1000,500)