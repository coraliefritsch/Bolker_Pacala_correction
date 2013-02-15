# -*- coding:Utf-8 -*-
import numpy as np
import classe_individu as CI
import classe_parametres

class population(object):
    'une population est un ensemble d individus'
    def __init__(self,param):
        '''
            une population contient 2 arguments :
            
                .taille qui est le nombre d'individus de la population
                
                .individus qui est une liste de taille 
                param.taille_maximale_de_la_population (allocation de mémoire)
                    les self.taille premiers éléments de la liste sont les 
                    individus de la population distibués uniformément sur le 
                    tore [0,Lx]x[0,Ly] (où Lx et Ly sont des arguments de param 
                    (de la classe paramètres)) les autres sont des éléments 
                    quelconques de type "individu"
                    
        attention : le nombre de voisins de chaque individu doit être calculé
        '''
        n=param.taille_initiale_de_la_population
        #allocation de mémoire :
        self.individus=[CI.individu(0,0)]*param.taille_maximale_de_la_population  
        #on tire n individus, uniformément dans le domaine :
        self.individus[:n]=[CI.individu(param.Lx*np.random.random(),
                                        param.Ly*np.random.random()) 
                            for i in range(n)]
        self.taille=n
        # on calcule le nombre de voisins de chaque individu créé :
        for ind in self.individus[:self.taille]:
            ind.nbvoisins=ind.nombre_de_voisins(self,param)
    
    def tuer(self,i,param):
        '''retire l’individu numéro i de la population self
            et change le nombre de voisins des autres individus de la 
            population (si nécessaire)
        '''
        #on diminue le nombre de voisins de chaque voisin de l'individu que 
        #l'on tue :
        for ind in self.individus[:self.taille]:
            if (self.individus[i].distance(ind,param)
                <=param.rayon_du_noyau_de_competition):
                ind.nbvoisins=ind.nbvoisins-1
        #on enlève l'individu de la population en le remplaçant par le dernier 
        #individu du tableau d'individus
        self.taille=self.taille-1
        self.individus[i]=self.individus[self.taille]
        
    def ajouter(self,ind,param):
        '''ajoute l’individu ind=((x,y),0) à la population
            et change le nombre de voisins des individus (ind compris) de la
            population (si nécessaire)
        '''
        #on augemente le nombre de voisins de chaque voisin du nouvel individu :
        for indi in self.individus[:self.taille]:
            if indi.distance(ind,param)<=param.rayon_du_noyau_de_competition:
                indi.nbvoisins=indi.nbvoisins+1
                ind.nbvoisins=ind.nbvoisins+1
        #on ajoute le nouvel individu (dont le nombre de voisins a été calculé 
        #dans la boucle précédente) à la population :
        self.individus[self.taille]=ind   
        self.taille=self.taille+1