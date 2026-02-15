import numpy as np
from math import *
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy
import time


## Exercice 1

def simulation_Tn(Lambda,n):
    Ech=stats.expon.rvs(scale=1/Lambda, size=n)
    return(np.sum(Ech))

N=1000
l=12
n=500
Ech=[simulation_Tn(l,n) for i in range (N)]
T=np.linspace(min(Ech),max(Ech), 250)
D=stats.gamma.pdf(T,a=n,loc=0,scale=1/l)
plt.plot(T,D)
plt.hist(Ech,density=True)
plt.show()

# On aurait aussi pu faire un test, cf prochain TP


## Exercice 2

## Question 1

def trajectoire_Poisson(n,l,b): # si b==1, on affiche la trajectoire, sinon on la renvoie
    X=stats.expon.rvs(loc=0,scale=1/l,size=n)
    T=np.array([0]+list(np.cumsum(X)))
    N=np.arange(n+1)
    if b==1 :
        plt.plot(T,N,drawstyle='steps-post')
        plt.title('Simulation de trajectoire de processus de Poisson')
        plt.show()
    else :
        return(T,N)


trajectoire_Poisson(20,1/5,1)

# Pour vérifier que le résultat est cohérent, il faut regarder en moyenne la fréquence des sauts (ici il faut environ 100 unités de temps pour faire 20 sauts, ça paraît ok)

## Question 2a)

def trajectoire_Poisson2(t,l,b): # si b==1, on affiche la trajectoire, sinon on la renvoie
    T=[0]
    x=0
    N=[0]
    n=0
    while t>x:
        x+=stats.expon.rvs(loc=0,scale=1/l)
        T.append(x)
        n+=1
        N.append(n)
    T[-1]=t
    N[-1]=N[-2] # ces deux lignes servent à s'arrêter à t, et non au premier saut après t
    if b==1:
        plt.plot(T,N,drawstyle='steps-post')
        plt.title('Simulation de trajectoire de processus de Poisson')
        plt.show()
    else :
        return(T,N)

trajectoire_Poisson2(20,1/5,1)

# On obtient 4 sauts en moyenne : cohérent.

## Question 2b)

def trajectoire_Poisson3(t,l,b): # si b==1, on affiche la trajectoire, sinon on la renvoie
    k=stats.poisson.rvs(mu=l*t)
    U=stats.uniform.rvs(loc=0,scale=t,size=k)
    T=[0]+list(np.sort(U))+[t]
    N=list(np.arange(k+1))+[k]
    if b==1 :
        plt.plot(T,N,drawstyle='steps-post')
        plt.title('Simulation de trajectoire de processus de Poisson')
        plt.show()
    else :
        return(T,N)

trajectoire_Poisson3(20,1/5,1)

# De même, on obtient 4 sauts en moyenne.

## Comparaison temps de calcul

N=100

# Première méthode :

t0=time.perf_counter()

T=[]
for _ in range (N):
    T=trajectoire_Poisson2(20,1/5,0)

t1=time.perf_counter()

print(t1-t0)

# Deuxième méthode

t0=time.perf_counter()

T=[]
for _ in range (N):
    T=trajectoire_Poisson3(20,1/5,0)

t1=time.perf_counter()

print(t1-t0)

# La deuxième méthode est plus rapide.

## Question 3

def illustration_Poisson(t,l,N): # N est le nombre de simulations
    Nt=[]
    for _ in range (N):
        T,N= trajectoire_Poisson2(t,l,0)
        Nt.append(N[-1])
    Nt=np.array(Nt)
    I=np.arange(max(Nt)+1)
    P_emp=[np.mean(Nt==i) for i in I]
    P_th=stats.poisson.pmf(I, mu=l*t)
    plt.bar(I-0.1,P_emp,0.3,label='fréquences empiriques de Nt')
    plt.bar(I+0.1,P_th,0.3,label='loi de Poisson')
    plt.title('Comparaison loi de Nt et loi de Poisson ')
    plt.legend()
    plt.show()

illustration_Poisson(20,1/5,500)

## Question 4

N=1000
l=1/5
t=20
m=11
I=np.arange(m)
Pm=stats.poisson.pmf(I, mu=l*t)
print([N*Pm>=5]) # on choisit m pour ne pas avoir à regrouper de cases (il faut un vecteur de True)


Nt=[]
for _ in range (N):
    T0,N0= trajectoire_Poisson2(t,l,0)
    Nt.append(N0[-1])
I2=np.arange(max(Nt)+1)
F=np.array([np.mean(Nt==i) for i in I2])

P_emp=np.array(list(F[:m])+[np.sum(F[m:])]) # on regroupe après m

P_th=np.array(list(Pm)+[1-np.sum(Pm)]) # on regroupe après m également

if len(P_emp)==len(P_th):
    D,p=stats.chisquare(N*P_emp,N*P_th)
    print(p)
# on ne rejette pas H0 (p valeur largement au dessus de alpha = 0.05)

# Certaines simulations échouent quand le max de Nt est inférieur à m (et donc len(P_emp)!=len(P_th)). On peut corriger en ajoutant des zéros sur les cases restantes de P_emp, je ne le fais pas pour ne pas alourdir le code déjà lourd.


## Exercice 3

##Question 1

# On estime cette espérance grâce à la méthode de Monte-Carlo

def esperance_intervalle(t,l,N): # N est le nombre de simulations
    I=[]
    for _ in range (N):
        T=[0]
        x=0
        while x<=t:
            x+=stats.expon.rvs(scale=1/l)
            T.append(x)
        int=T[-1]-T[-2]
        I.append(int)
    return(np.mean(np.array(I)))

l=1/5
t=20
E_emp=esperance_intervalle(t,l,1000)
E_th=(2-np.exp(-l*t))/l
print(E_emp)
print(E_th)

## Question 2

# Les temps inter-sauts suivent des lois exponentielles, et ont donc 1/lambda pour moyenne, qui est strictement inférieur à la moyenne obtenue dans la question précédente : c'est le paradoxe de l'autobus. Le temps attendu est en moyenne plus grand que le temps moyen entre deux bus. Mais cela s'explique par le fait que l'on "voit plus" les longues périodes entre 2 bus; pensez à un gâteau qui aurait des parts inégales, a priori si l'on pointe une part au hasard sur le gâteau, on a plus de chances de tomber sur une grosse part parce qu'on "les voit plus".


## Exercice 4
# (n'hésitez pas à aller le voir le récap pour cet exo, les maths y sont plus proprement écrites)

## Question 1

l=stats.expon.rvs(scale=1) # faites ce qui vous fait plaisir

## Question 2

# D'après la loi des grands nombres fournie, un estimateur de lambda est donné par \hat{\lambda_t}:= \frac{N_t}{t}.

## Question 3

# En utilisant le lemme de Slutsky, on obtient : \sqrt{\frac{t}{\hat{\lambda_t}}} \left ( \hat{\lambda_t} - \lambda \right) converge en loi vers une normale centrée réduite.
# Et ainsi un intervalle de confiance (asymptotique) de niveau de confiance $\alpha$ est donné par :
# $$ I_\alpha := \left [  \widehat{\lambda_t} -  q_{1 - \alpha/2}\sqrt{\frac{\widehat{\lambda_t}}{t}} , \widehat{\lambda_t} + q_{1 - \alpha/2} \sqrt{\frac{\widehat{\lambda_t}}{t}}  \right ], $$
# où $q_{1 - \alpha/2}$ est le quantile d'ordre $1 -\alpha /2$ d'une loi normale centrée réduite.

## Question 4

def illustration_convergence(t_max,l,alpha):
    T,N=trajectoire_Poisson3(t_max,l,0)
    temps=np.linspace(50,t_max,200)
    E=[]
    I_inf=[]
    I_sup=[]
    q= stats.norm.ppf(1-alpha/2,loc=0,scale=1)
    for s in temps :
        e=np.sum([T<=s])/s
        E.append(e)
        i_inf=e-np.sqrt(e/s)*q
        I_inf.append(i_inf)
        i_sup=e+np.sqrt(e/s)*q
        I_sup.append(i_sup)
    L=l*np.ones(len(temps))
    plt.plot(temps,E,label='estimateur')
    plt.plot(temps,I_inf,label='borne inf intervalle')
    plt.plot(temps,I_sup,label='borne sup intervalle')
    plt.plot(temps,L,label='valeur théorique de lambda')
    plt.legend()
    plt.show()

illustration_convergence(1000,l,0.05)

## Question bonus

# Illustration du TCL obtenu en question 3 grâce à Slutsky

def illustration_TCL_bonus(t,l,N):
    H=[]
    for _ in range (N):
        T,N=trajectoire_Poisson3(t,l,0)
        e=N[-1]/t
        h=np.sqrt(t/e)*(e-l)
        H.append(h)
    X=np.linspace(min(H),max(H),200)
    Y=stats.norm.pdf(X)
    plt.hist(H,25,density='True', label='histogramme échantillon')
    plt.plot(X,Y,label='densité loi normale')
    plt.title('Illustration du TCL obtenu via un histogramme')
    plt.legend()
    plt.show()

illustration_TCL_bonus(1000,l,1000)


## Exercice 5
# (de nouveau ici, pour les maths, cf le récap pour plus de clarté)

## Question 1

l=stats.expon.rvs(scale=1)

## Question 2

# D'après la loi des grands nombres fournie, un estimateur de lambda est donné par \hat{\lambda_n}:= \frac{T_n}{n}.

## Question 3

# Un intervalle de confiance (asymptotique) de niveau de confiance $\alpha$ est donné par :
# $$I_\alpha := \left [ \frac{1}{\widehat{\lambda_n}}( 1 - \sqrt n q_{1 - \alpha/2}), \frac{1}{\widehat{\lambda_n}}( 1 + \sqrt n q_{1 - \alpha/2}) \right ]. $$

## Question 4

def illustration_convergence2(n,l,alpha):
    T,N=trajectoire_Poisson(n,l,0)
    print(T)
    E=[]
    I_inf=[]
    I_sup=[]
    q= stats.norm.ppf(1-alpha/2,loc=0,scale=1)
    for k in N[50:] :
        e=k/T[k]
        E.append(e)
        i_inf=e*(1-q/np.sqrt(k))
        I_inf.append(i_inf)
        i_sup=e*(1+q/np.sqrt(k))
        I_sup.append(i_sup)
    L=l*np.ones(len(N[50:]))
    plt.plot(N[50:],E,label='estimateur')
    plt.plot(N[50:],I_inf,label='borne inf intervalle')
    plt.plot(N[50:],I_sup,label='borne sup intervalle')
    plt.plot(N[50:],L,label='valeur théorique de lambda')
    plt.legend()
    plt.show()

illustration_convergence2(10000,l,0.05)

## Question bonus

# Illustration du TCL

def illustration_TCL_bonus2(n,l,N):
    H=[]
    for _ in range (N):
        T,N=trajectoire_Poisson(n,l,0)
        e=T[-1]/n
        h=np.sqrt(n)*(l*e-1)
        H.append(h)
    X=np.linspace(min(H),max(H),200)
    Y=stats.norm.pdf(X)
    plt.hist(H,25,density='True', label='histogramme échantillon')
    plt.plot(X,Y,label='densité loi normale')
    plt.title('Illustration du TCL via un histogramme')
    plt.legend()
    plt.show()

illustration_TCL_bonus2(1000,l,1000)


## Exercice 6

# La question n'est pas très précise... on va par exemple illustrer que, en notant Zt= Mt+Nt, Zt suit une loi de Poisson de paramètre (lambda+mu)*t (en utilisant la première méthode de simulation sinon cela n'a aucun intérêt...)

def illustration_superposition(t,l,m,N):
    E=[]
    for _ in range (N):
        N_l=0
        x_l=0
        while t>x_l:
            x_l+=stats.expon.rvs(loc=0,scale=1/l)
            N_l+=1
        N_m=0
        x_m=0
        while t>x_m:
            x_m+=stats.expon.rvs(loc=0,scale=1/m)
            N_m+=1
        E.append(N_m-1+N_l-1)
    I=np.arange(max(E)+1)
    P_emp=[np.mean(E==i) for i in I]
    P_th=stats.poisson.pmf(I, mu=(l+m)*t)
    plt.bar(I-0.1,P_emp,0.3,label='fréquences empiriques de Nt+Mt')
    plt.bar(I+0.1,P_th,0.3,label='loi de Poisson de paramètre lambda+mu')
    plt.title('Illustration superposition')
    plt.legend()
    plt.show()

illustration_superposition(20,1/3,1/5,1000)


## Exercice 7

def illustration_decomposition(t,l,p):
    T,N=trajectoire_Poisson2(t,l,0)
    N1=[0]
    N2=[0]
    for j in range(len(T)-1):
        x=stats.binom.rvs(n=1, p=p)
        print(x)
        if x==1:
            N1.append(N1[-1]+1)
            N2.append(N2[-1])
        else:
            N2.append(N2[-1]+1)
            N1.append(N1[-1])
    plt.plot(T,N,drawstyle='steps-post',label='N')
    plt.plot(T,N1,drawstyle='steps-post', label='N1')
    plt.plot(T,N2,drawstyle='steps-post', label='N2')
    plt.title('Illustration décomposition')
    plt.legend()
    plt.show()

illustration_decomposition(100,1/5,0.7)


## Exercice 8

def trajectoire_Poisson_composé_normale(t,l,m,sigma,b): # simule jusqu'à t
    k=stats.poisson.rvs(mu=l*t)
    U=stats.uniform.rvs(loc=0,scale=t,size=k)
    T=[0]+list(np.sort(U))+[t]
    Y=stats.norm.rvs(loc=m,scale=sigma, size=k)
    X=np.array([0]+list(np.cumsum(Y))+[np.sum(Y)])
    if b==1:
        plt.plot(T,X,drawstyle='steps-post')
        plt.title('Simulation de trajectoire de processus de Poisson composé')
        plt.show()
    else :
        return(T,X)

trajectoire_Poisson_composé_normale(100,1/3,0,1,1)


# Puisque cela servira à la question suivante, voilà une simulation de trajectoire dans le cas où la loi de saut est une exponentielle :

def trajectoire_Poisson_composé_expo(t,l,m,b): # simule jusqu'à t
    k=stats.poisson.rvs(mu=l*t)
    U=stats.uniform.rvs(loc=0,scale=t,size=k)
    T=[0]+list(np.sort(U))+[t]
    Y=stats.expon.rvs(scale=1/m, size=k)
    X=np.array([0]+list(np.cumsum(Y))+[np.sum(Y)])
    if b==1:
        plt.plot(T,X,drawstyle='steps-post')
        plt.title('Simulation de trajectoire de processus de Poisson composé')
        plt.show()
    else :
        return(T,X)

trajectoire_Poisson_composé_expo(100,1/3,2,1)


## Exercice 9

# On utilise la méthode de Monte Carlo

## Premier exemple avec une loi de saut normale :

def illustration_corollaire_normale(t,l,m,sigma,N):
    E=[]
    for _ in range(N):
        T,X=trajectoire_Poisson_composé_normale(t,l,m,sigma,0)
        E.append(X[-1])
    E=np.array(E)
    m_emp=np.mean(E)
    v_emp=(1/(N-1))*np.sum((E-m_emp)**2)
    return(m_emp,v_emp)

N=1000
t=20
l=1/3
m=5
sigma=2
m_th=m*l*t
v_th=l*t*(sigma**2)+l*t*(m**2)
m_emp,v_emp=illustration_corollaire_normale(t,l,m,sigma,N)
print('comparatif moyenne',m_th,m_emp)
print('comparatif variance', v_th,v_emp)

## Deuxième exemple avec une loi exponentielle :

def illustration_corollaire_expo(t,l,m,N):
    E=[]
    for _ in range(N):
        T,X=trajectoire_Poisson_composé_expo(t,l,m,0)
        E.append(X[-1])
    E=np.array(E)
    m_emp=np.mean(E)
    v_emp=(1/(N-1))*np.sum((E-m_emp)**2)
    return(m_emp,v_emp)

N=1000
t=20
l=1/3
m=2
m_th=m*l*t
v_th=l*t*(sigma**2)+l*t*(m**2)
m_emp,v_emp=illustration_corollaire_expo(t,l,1/m,N) # attention, dans le code, m est le paramètre et non la moyenne (doù le 1/m)
print('comparatif moyenne',m_th,m_emp)
print('comparatif variance', v_th,v_emp)

