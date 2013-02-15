# -*- coding:Utf-8 -*-
import numpy as np
import random
import pylab as pl
import classe_parametres as CPa
import classe_population as CPo
import fonctions as fct
        
random.seed(0)  #initialise le générateur de nombres aléatoires

        
############ INITIALISATION ############        
parametres = CPa.parametres()  #on récupère les paramètres du modèle
pop = CPo.population(parametres) #initialisation de la popualation
temps=0                                 #temps représente le temps courant
############ /INITIALISATION ############


#Constante de calcul :
taux_fixe=parametres.taux_de_reproduction+parametres.taux_de_mort_naturelle


#Affichage graphique de la population initiale :
pl.ion()    #affichage dynamique
fct.affichage_graphique_de_la_population(pop,parametres.Lx, parametres.Ly,0)

############ ITERATIONS ############
#Les évènements ont lieu tant que le temps maximal n'est pas atteint, que la 
#population ne s'est pas éteinte et que la population n'a pas atteint la taille 
#maximale qu'on lui a imposée
while (temps<parametres.temps_max and pop.taille>0 
       and pop.taille<parametres.taille_maximale_de_la_population):
    #On calcule le taux de compétition  subit par chaque individu : Il 
    #correspond au nombre de voisins de l'individu * taux de stress engendré 
    #par un voisin 
    #Le taux de saut global de la population est alors:
    #    taux_global=taux_fixe*N+somme(competition des individus)
    #On tire le temps du prochain évènement par une loi exponentielle de 
    #taux taux_global. On décide ensuite le saut de la population (mort ou 
    #naissance) par la fonction saut.
    competition = (parametres.taux_de_mort_par_competition
                   *np.array([ind.nbvoisins 
                              for ind in pop.individus[:pop.taille]]))
    t = random.expovariate(pop.taille*taux_fixe+np.sum(competition))
    temps = temps+t

    
    i = fct.choix_individu(competition+taux_fixe)
    fct.saut(pop,i,competition[i]+taux_fixe,parametres)
    
    fct.affichage_graphique_de_la_population(pop,parametres.Lx,
                                              parametres.Ly,temps)
    
############ /ITERATIONS ############


pl.ioff()   #pour arrêter l'affichage dynamique
fct.affichage_graphique_de_la_population(pop,parametres.Lx, parametres.Ly,temps)
pl.show()

#Affichage d'un message en cas d'extinction de la population  
if pop.taille==0:
    print "extinction de la population"   


