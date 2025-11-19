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
        estim=i/np.sum(T[:i])
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

# $\frac{\sqrt n}{\lambda} \left(\frac{n}{S_n} - \lambda \right) \xrightarrow[n \to \infty]{\mathcal L } \mathcal N (0,1) $

## Question 2

def illustration_cv_loi_fdr_exp(l,n,N):
    M=stats.expon.rvs(scale=1/l,size=(N,n))
    E=(sqrt(n)/l)*((n/np.sum(M,axis=1))-l)
    E=np.sort(E)
    F_emp=np.arange(1,N+1)/N
    plt.plot(E,F_emp,drawstyle='steps-pre',label='Fonction de répartition empirique')

    X = np.linspace(min(E),max(E),500)
    F_th=stats.norm.cdf(X)
    plt.plot(X,F_th,label='Fonction de répartition théorique')

    plt.title('Illustration de la convergence en loi via les fonctions de répartition')
    plt.legend()
    plt.show()

illustration_cv_loi_fdr_exp(2,500,100)


def illustration_cv_loi_fdr_exp_bis(l,n,N): # version avec une boucle for
    E=[]
    for _ in range (N):
        X=stats.expon.rvs(scale=1/l,size=n)
        E.append((sqrt(n)/l)*((n/np.sum(X))-l))
    E=np.sort(E)
    F_emp=np.arange(1,N+1)/N
    plt.plot(E,F_emp,drawstyle='steps-pre',label='Fonction de répartition empirique')

    X = np.linspace(min(E),max(E),500)
    F_th=stats.norm.cdf(X)
    plt.plot(X,F_th,label='Fonction de répartition théorique')

    plt.title('Illustration de la convergence en loi via les fonctions de répartition')
    plt.legend()
    plt.show()

#illustration_cv_loi_fdr_exp_bis(2,500,100)

## Question 3

def illustration_cv_loi_hist_exp(l,n,N): # n est la taille des échantillons, et N le nombre des échantillons
    M=stats.expon.rvs(scale=1/l,size=(N,n))
    L=(sqrt(n)/l)*((n/np.sum(M,axis=1))-l)
    X=np.linspace(min(L),max(L),200)
    Y=stats.norm.pdf(X)
    plt.hist(L,25,density='True', label='histogramme échantillon')
    plt.plot(X,Y,label='densité loi normale')
    plt.title('Illustration de la convergence en loi via un histogramme')
    plt.legend()
    plt.show()

illustration_cv_loi_hist_exp(2,1000,500)


def illustration_cv_loi_hist_exp_bis(l,n,N):  # version avec une boucle for
    L=[]
    for _ in range(N):
        X=stats.expon.rvs(scale=1/l,size=n)
        L.append((sqrt(n)/l)*((n/np.sum(X))-l))
    X=np.linspace(min(L),max(L),200)
    Y=stats.norm.pdf(X)
    plt.hist(L,25,density='True', label='histogramme échantillon')
    plt.plot(X,Y,label='densité loi normale')
    plt.title('Illustration de la convergence en loi via un histogramme')
    plt.legend()
    plt.show()

#illustration_cv_loi_hist_exp_bis(2,1000,500)

