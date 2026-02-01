import numpy as np
from math import *
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy.special as special
import scipy
import time


## Programme simulation chaîne de Markov

def trajectoire_markov(n,P,x0):
    X=np.zeros(n,dtype=int) #on indique que X contiendra seulement des entiers.
    X[0]=x0
    for k in range(n-1):
        X[k+1]=np.random.choice(a=range(len(P)), p=P[X[k],:])
        # Les états sont numérotés de 0 à len(P)-1
    return (X)

## Exemple avec marche sur Z

def marche_aleatoire(n,p): # simule la trajectoire d'une marche aléatoire sur Z de proba p de monter et 1-p de descendre
    pas=2*stats.binom.rvs(1,p,size=n)-1
    position=np.cumsum(pas)
    return(position)

def illustration_marche_aleatoire(n,p): # affiche la trajectoire d'une marche aléatoire sur Z de proba p
    P=np.zeros(n+1)
    P[1:]=marche_aleatoire(n,p)
    plt.plot(np.arange(n+1),P)
    plt.xlabel("Nombre d'étapes")
    plt.ylabel("Position")
    plt.title("Simulation d'une marche aléatoire sur Z")
    plt.show()

illustration_marche_aleatoire(1000,0.5)


## Exercice 1

##Question 1

def matrice_transition(N):
    P=np.array([[comb(N,j)*((i/N)**j)*((1-(i/N))**(N-j)) for j in range (N+1)] for i in range (N+1)])
    return(P)

# pour vérifier que ce que l'on a codé est au moins une matrice de transition:
print(np.sum(matrice_transition(10), axis=1))
print(matrice_transition(3))

##Question 2 (j'ai directement intégré la question 4 avec les temps de calcul)

def trajectoire1(k,N,n):
    t0=time.perf_counter()
    P=matrice_transition(N)
    X=trajectoire_markov(n,P,k)
    t1=time.perf_counter()
    return(X,t1-t0)

n=100
X1,t1=trajectoire1(5,10,n)
print(t1)
T=np.arange(n)
plt.plot(T,X1)
plt.xlabel('k')
plt.ylabel('position de la chaîne au temps k ')
plt.title('Exemple de trajectoires du modèle de Wright-Fisher')
plt.show()

##Question 3

def trajectoire2(k,N,n):
    t0=time.perf_counter()
    X=np.zeros(n,dtype=int)
    X[0]=k
    for k in range(n-1):
        X[k+1]=stats.binom.rvs(n=N,p=(X[k]/N))
    t1=time.perf_counter()
    return(X,t1-t0)

n=100
X2,t2=trajectoire2(5,10,n)
print(t2)
T=np.arange(0,n)
plt.plot(T,X2)
plt.xlabel('k')
plt.ylabel('position de la chaîne au temps k ')
plt.title('Exemple de trajectoires du modèle de Wright-Fisher')
plt.show()

#La premère méthode est un peu plus rapide


## Exercice 2

## Question 1

# C'est une chaîne de Markov homogène. Elle n'a qu'une seule classe d'équivalence, elle est donc irréductible, et ainsi tous les états sont de même nature. Etant donné que l'espace d'états est fini, les états sont tous réccurents positifs. Le coefficient P_{1,1} est non nul (i.e on peut boucler sur 1), et puisque il n'y a qu'une seule classe d'équivalence, la chaîne est apériodique.

# Comme la chaîne est irréductible, et que tous les états sont récurrents positifs, la chaîne a une unique probabilité invariante. A partir de là, il existe plusieurs possibilités pour l'obtenir numériquement, nous verrons cela en question 4.

## Question 2

P_Grib= np.array([[0.9,0.05,0.05],[0.7,0,0.3],[0.8,0,0.2]])
# on code (0,1,2) pour (dormir, manger, jouer).

def proba(n,k1,k2):
    #proba d'être en k2 au bout de N états en étant parti de k1
    A=np.linalg.matrix_power(P_Grib,n) # P**n ne renvoie pas P à la puissance n, mais la matrice dont les coefficients sont les coefficents de P mis à la puissance n
    return(A[k1][k2])

print(proba(7,0,2))
print(proba(42,1,0))

## Question 3

def vecteur_proba(n,k): # renvoie les probas de la chaîne à l'étape n sachant qu'elle est partie de l'état k
    A=np.linalg.matrix_power(P_Grib,n)
    return(A[k])

print(vecteur_proba(10,1))
print(vecteur_proba(25,1))
print(vecteur_proba(50,1))
print(vecteur_proba(100,1))

# Il y a effectivement convergence des puissances de P : la chaîne est irréductible et apériodique donc elle converge en loi vers sa mesure invariante, et ce peu importe la loi initiale.

## Question 4

# Pour déterminer la proba invariante \pi de notre chaîne, au vu de la situation, on dispose de 3 méthodes. La première, c'est d'utiliser la définition: le vecteur \pi vérifie l'équation \pi P = \pi, autrement, \pi est vecteur propre de la transposée de P pour la valeur propre 1.

def proba_invariante1(P):
    eigVal,eigVec= np.linalg.eig(P.T)
    i=np.where(abs(eigVal-1)< 0.001)[0][0] # il faut faire attention aux erreurs de calcul etc
    p=np.real(eigVec[:,i]) # on prend le vecteur propre associé à 1, attention il est en colonne
    return(p/np.sum(p)) #attention il faut normaliser le vecteur !

pi1= proba_invariante1(P_Grib)
print(pi1, np.sum(pi1))

# La deuxième méthode, c'est d'utiliser la convergence en loi de la chaîne vers sa proba invariante (cf question précédente), qui nous dit que pour n'importe quelle loi initiale \mu, on a \mu P^n converge vers \pi.

def proba_invariante2(P,N):
    A=np.linalg.matrix_power(P,N)
    n=len(P)
    mu=np.ones(n)/n # on peut mettre ce que l'on veut comme loi initiale, ici je mets la loi uniforme
    pi=mu.dot(A)
    pi[-1]=1-np.sum(pi[:-1]) # pour que le vecteur se somme à 1
    return(pi)

pi2=proba_invariante2(P_Grib,100)
print(pi2, np.sum(pi2))

# La troisième méthode s'appuie sur le théorème ergodique, qui s'applique car la chaîne est irréductible et réccurente positive. On sait donc que le vecteur des fréquences de passage converge vers la proba invariante.

def proba_invariante3(n,P,x0): # ici, la loi initiale est le Dirac en x0, mais on aurait pu mettre n'importe quelle autre loi initiale
    X=trajectoire_markov(n,P,x0)
    P=np.array([np.mean(X==i) for i in range (len(P))])
    return(P)

pi3= proba_invariante3(10000,P_Grib,0)
print(pi3, np.sum(pi3)) # moins précis


## Exercice 3

## Question 1

# Déjà fait à la question précédente, c'est l'avantage de coder avec des fonctions ^^

## Question 2

# Il suffit de dessiner un graphe connexe à 5 éléments avec des poids, et d'en écrire la matrice. La chaine sera irréductible et comme elle est à espace d'états fini, elle sera récurrente positive. Pour qu'elle soit apériodique, il suffit qu'au moins un état puisse boucler sur lui même, i.e. qu'il existe un indice i tel que le coefficient P_{i,i} soit non nul. Par exemple :

P5=np.array([[1/2,1/2,0,0,0],[0,0,1/3,1/3,1/3],[1/2,0,0,1/2,0],[0,0,0,1/4,3/4],[0,0,2/3,0,1/3]])

pi=proba_invariante1(P5)
print(pi, np.sum(pi))

## Question 3

def distance(P,n):
    pi=proba_invariante1(P)
    PI=np.array([pi for i in range (len(pi))])
    Pn=np.linalg.matrix_power(P,n)
    d=np.linalg.norm(Pn-PI,np.inf) # calcul de la norme infinie
    return(d)

print(distance(P5,30))

def representation_distance(P,n): #representation de log(d_k)/k jusqu'à n
    pi=proba_invariante1(P)
    PI=np.array([pi for i in range (len(pi))])
    D=np.zeros(n)
    N=np.arange(1,n+1)
    A=np.eye(len(P)) #va prendre les valeurs successives de P^i
    for i in N:
        A=A.dot(P)
        d=np.log(np.linalg.norm(A-PI,np.inf))/i
        D[i-1]=d
    plt.plot(N,D)
    plt.title('log(d_k)/k en fonction de k')
    plt.show()

# Il ne faut pas prendre n trop grand: avec les erreurs d'approximation du calcul de la puissance et surtout de la différence avec PI, d devient constant mais pas nul au bout d'un moment et donc le 1/n écrase tout.

representation_distance(P5,40)

# Il existe un théorème qui nous donne une convergence exponentielle vers la mesure invariante, de l'ordre de log(gamma), où gamma est le plus grand module parmi les valeurs propres <1. Honnêtement, je ne le connais par par coeur... voir par exemple https://agreg-maths.univ-rennes1.fr/documentation/docs/Perron-Frobenius.pdf (ou probablement, les compléments de Matteo)


def representation_distance_comparaison_gamma(P,n): #representation de log(d_k)/k jusqu'à n
    pi=proba_invariante1(P)
    PI=np.array([pi for i in range (len(pi))])
    D=np.zeros(n)
    N=np.arange(1,n+1)
    A=np.eye(len(P)) #va prendre les valeurs successives de P^i
    for i in N:
        A=A.dot(P)
        d=np.log(np.linalg.norm(A-PI,np.inf))/i
        D[i-1]=d
    eigVal,eigVec= np.linalg.eig(P.T)
    m=np.abs(eigVal)
    gamma=np.max(m[1:])
    plt.plot(np.log(gamma)*np.ones(len(N)), label='ordre théorique de convergence')
    plt.plot(N,D,label='log(d_k)/k en fonction de k')
    plt.legend()
    plt.show()

representation_distance_comparaison_gamma(P5,40)
# Effectivement, ça a l'air de marcher !

## Question 4

def illustration_thm_ergodique(P,f,n,x0):
    pi=proba_invariante1(P)
    X=trajectoire_markov(n,P,x0)
    F=f(X)
    S=[]
    N=np.arange(50,n+1)
    E=np.arange(len(P)) #espace d'états
    I=np.sum(pi*f(E)) #valeur théorique de l'intégrale (le produit * pour 2 np.array fait le produit terme à terme)
    for i in N:
        Fi=F[:i]
        s=np.mean(Fi)
        S.append(s)
    plt.xlabel('N')
    plt.plot(N,S,label='estimation')
    plt.plot(N,I*np.ones(len(N)),label='valeur théorique')
    plt.title('Illustration du théorème ergodique')
    plt.legend()
    plt.show()

def f(x):
    return(x**2)

f=np.vectorize(f)

illustration_thm_ergodique(P5,f,10000,0)

# L'ordre des fluctuations est en \sqrt(n), et la limite en loi est une loi normale (TCL pour les chaînes de Markov). Pour le montrer, on va tracer un histogramme de (sqrt(n)(I_n-I), et juste constater avec nos petits yeux que ça ressemble effectivement à une gaussienne (parce que la variance limite est compliquée).

def ordre_fluctuation(P,f,n,N,x_0): # N est le nombre d'échantillons, n est leur taille
    H=[]
    pi=proba_invariante1(P)
    E=np.arange(len(P)) #espace d'états
    I=np.sum(pi*f(E)) #valeur théorique de l'intégrale
    for i in range (N):
        X=trajectoire_markov(n,P,x_0)
        F=f(X)
        s=np.mean(F)
        H.append(sqrt(n)*(s-I))
    H=np.array(H)
    plt.hist(H, bins=25, density=True, label='Histogramme échantillon')
    plt.title('Illustration du TCL pour les chaînes de Markov')
    plt.legend()
    plt.show()

#ordre_fluctuation(P5,f,2000,1000,0) # A partir de là, les simu deviennent toutes très longues...(surtout celle-ci)

## Question 5

def illustration_cv_loi(P,n,N,x0): # N est le nombre d'échantillons, n est leur taille
    p=np.zeros(len(P))
    pi=proba_invariante1(P)
    E=np.arange(len(P))
    for i in range (N):
        X=trajectoire_markov(n,P,x0)
        p[X[-1]]+=1
    p=p/N
    plt.bar(E-0.1,p,0.3,label='fréquences empiriques')
    plt.bar(E+0.1,pi,0.3,label='loi invariante')
    plt.title('Illustration de la convergence en loi ')
    plt.legend()
    plt.show()

illustration_cv_loi(P5,1000,1000,0)

def illustration_cv_variation_totale(P,n,N,x0): # N est le nombre d'échantillons, n est leur taille
    p=np.zeros(len(P))
    pi=proba_invariante1(P)
    E=np.arange(len(P))
    for i in range (N):
        X=trajectoire_markov(n,P,x0)
        p[X[-1]]+=1
    p=p/N
    d=np.sum(np.abs(p-pi))
    return(d)

print(illustration_cv_variation_totale(P5,1000,1000,0))

## Question 6

def temps_retour(P,x0): #simule une chaîne de Markov de matrice P, qui s'arrête dès qu'elle rencontre x0, en renvoyant l'indice de retour en x0
    X=[x0]
    X.append(np.random.choice(a=range(len(P)), p=P[X[0],:]))
    k=1
    while X[-1]!= x0:
        X.append(np.random.choice(a=range(len(P)), p=P[X[k],:]))
        k+=1
    return(k)

# On cherche ici à illustrer l'égalité pi(x)=1/E[T_x]

def illustration_egalite(P,N): # N est le nombre d'échantillons
    Esp=np.zeros(len(P))
    pi=proba_invariante1(P)
    E=np.arange(len(P))
    for i in range(len(P)):
        e=0
        for k in range (N):
            e+=temps_retour(P,i)
        Esp[i]=e/N
    plt.bar(E-0.1,1/Esp,0.3,label='inverse des moyennes empiriques de temps de retour')
    plt.bar(E+0.1,pi,0.3,label='loi invariante')
    plt.title('Illustration égalité considérée')
    plt.legend()
    plt.show()

illustration_egalite(P5,2000)


## Exercice 4

## Question 1

# On peut le modélise par une chaine de Markov à valeurs dans {0,1,2,..,7}, qui part de 3, et telle que sa matrice de transition P est donnée par la matrice suivante:

P=np.zeros((8,8))
P[0,0]=1
P[7,7]=1
for i in range(1,7):
    P[i,i-1]=0.6
    P[i,i+1]=0.4

## Question 2

# Il y a 3 classes d'equivalence (chaine non irréductible): {0}, {7} et le reste des états. Les états 0 et 7 sont absorbants, les autres sont transitoires. Les états 0 et 7 sont apériodiques et les autres sont de période 2.

## Question 3

def loi_tour(k): # donne la loi de la forturne de Pierre au bout du tour k
    A=np.linalg.matrix_power(P,k)
    return(A[3,:])

print(loi_tour(3))
print(loi_tour(10))
print(loi_tour(100))

# La valeur théorique est d'environ 0.147 (s'obtient par exemple en utilisant le système qui donne les probas d'absoprtion de chaque état par 7).

def absorption_victoire(): # renvoie 1 si on attend 7 avant 100 pas, et 0 sinon, pour une simulation de trajectoire
    X=[3]
    X.append(np.random.choice(a=range(len(P)), p=P[X[0],:]))
    k=1
    while X[-1]!= 7 and k<100:
        X.append(np.random.choice(a=range(len(P)), p=P[X[k],:]))
        k+=1
    return (X[-1]==7)

def estimation_proba_absorption_victoire(N): # estime la proba d'absorption par 7 avec une méthode de Monte-Carlo
    p=0
    for i in range (N):
        p+= absorption_victoire()
    return(p/N)

estimation_proba_absorption_victoire(1000)

## Question 4

# La valeur théorique est d'environ 9.83 (s'obtient par exemple en utilisant le système qui donne les temps moyens d'absorption de chaque état)

def temps_absorption(): # donne le temps d'attente avant d'être absorbé par 7 ou 0 pour une simulation de trajectoire
    X=[3]
    X.append(np.random.choice(a=range(len(P)), p=P[X[0],:]))
    k=1
    while X[-1]!= 0 and X[-1]!=7 and k<1000:
        X.append(np.random.choice(a=range(len(P)), p=P[X[k],:]))
        k+=1
    return(k)

def estimation_temps_absorption(N): # estime le temps moyen d'absorption par 7 ou 0 avec une méthode de Monte-Carlo
    e=0
    for i in range (N):
        e+=temps_absorption()
    return(e/N)

estimation_temps_absorption(5000)

## Question 5

# La valeur théorique est d'environ 11.72 (s'obtient par exemple en utilisant le système qui donne les temps moyens d'absorption par 7 sachant que celui-ci est fini pour chaque état, et en divisant le résultat obtenu pour l'état 3 par la probabilité d'être absorbé par 7 calculée à la question 3)

def temps_absorption_victoire(): # donne le temps d'attente avant d'être absorbé par 7, si l'on est effectivement absorbé par 7, pour une simulation de trajectoire : on renvoie donc le temps d'attente si l'on a été absorbé par 7, et 0 sinon (pour ne pas compter les cas d'absorption par 0)
    X=[3]
    X.append(np.random.choice(a=range(len(P)), p=P[X[0],:]))
    k=1
    while X[-1]!= 0 and X[-1]!=7 and k<100:
        X.append(np.random.choice(a=range(len(P)), p=P[X[k],:]))
        k+=1
    if X[-1]==7:
        return((k,True)) # on indique si la trajectoire est à prendre en compte ou non
    else:
        return((0,False))

def estimation_temps_absorption_victoire(N): # estime le temps moyen d'absorption par 7, si l'on est effectivement absorbé par 7, avec une méthode de Monte-Carlo
    e=0
    n=0
    for i in range (N):
        (t,B)=temps_absorption_victoire()
        if B==True:
            n+=1
            e+=t
    return(e/n)

estimation_temps_absorption_victoire(5000)


## Exercice 5

# Emeline avait mis dans sa correction un lien qui ne fonctionne plus, et cela ne me semble pas essentiel. Au besoin si quelqu'un est intéressé.e je peux y réfléchir plus intensément, ou chercher un module sur les graphes qui sait faire ce genre de choses, ça doit probablement exister.