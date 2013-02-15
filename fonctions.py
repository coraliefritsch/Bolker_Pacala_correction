# -*- coding:Utf-8 -*-

#Ce fichier comporte les trois fonctions:
#    - la fonction choix_individu qui tire l'individu qui subit l'évènement
#    - la fonction saut qui décide quel évènement subit l'individu tiré 
#        précédemment
#    - la fonction affichage_graphique_de_la_population qui gére l'affichage 
#        dynamique de la population

import numpy as np
import random
import pylab as pl

def choix_individu(taux_individus):
    '''choisit un individu dans la population en fonction des taux des individus
    ici taux_individus est un vecteur :
        taux_individus[i] est le taux global associé à l'individu numéro i
    la probabilité, pour un individu, d'être choisi est proportionnelle au 
    taux_global de cet individu
        
        exemple : 
            on a 5 individus de taux globaux respectifs : 1, 3, 8, 2, 0.5
            alors la probabilité pour l'individu numéro 
            - 0 est 1/(1+3+8+2+0.5)
            - 1 est 3/(1+3+8+2+0.5)
            - 2 est 8/(1+3+8+2+0.5)
            - 3 est 2/(1+3+8+2+0.5)
            - 4 est 0.5/(1+3+8+2+0.5)
            
            la fonction choix_individu tire un individu suivant la loi donnée 
            précédemment et renvoie le numéro de l'individu choisi (ici 0, 1, 
            2, 3 ou 4)
    '''
    u = random.random()
    taux_global = np.sum(taux_individus)
    return np.sum(np.cumsum(taux_individus/taux_global)<u)

        
def saut(pop,i,taux_i, param):
    #taux_i est le taux glabal de l'individu i :     
    #    taux_de_naissance+taux_de_mort+taux_competition*Nvoisins
    '''décide l’évènement (naissance ou mort) subit par l’individu numéro i de 
    la population pop, et modifie la population pop. L'évènement choisi dépend 
    de paramètres contenus dans param (class paramètres)
    
    exemple :
        Si un individu à pour taux global 5 et que le taux de naissance 
        (contenu dans param) est 2, alors
            - avec probabilité 2/5 il donne naissance à un nouvel individu
            - avec probabilité 3/5 il meurt (soit de mort naturelle, soit de 
            mort par compétition)
    ''' 
    u = random.random()   #u suit une loi U([0,1])
    if u<(param.taux_de_reproduction/taux_i):   #naissance
        y = pop.individus[i].naissance(param)   #y est le nouvel individu
        pop.ajouter(y,param)
    else:                                       #mort
        pop.tuer(i,param)


def affichage_graphique_de_la_population(pop,Lx,Ly,tps):
    'dessine la population pop dans le domaine [0,Lx]x[0,Ly] au temps t'
    pl.clf()    #efface le graphique précédent
    
    #Pour dessiner la population, on crée deux vecteurs : coordonnées en x et 
    #coordonnées en y des individus 
    pl.plot([ind.x for ind in pop.individus[:pop.taille]],
             [ind.y for ind in pop.individus[:pop.taille]],"o")
    
    pl.xlim([0,Lx]) #fixe l'axe des abscisses
    pl.ylim([0,Ly]) #fixe l'axe des ordonnées
    pl.title("Temps={0}, Nombre d'individus={1}".format(tps,pop.taille))
    pl.draw()   #dessine le graphique



