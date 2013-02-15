# -*- coding:Utf-8 -*-
class parametres(object):
    #Les differents paramètres de l'algorithme: 
    #Les individus vivent dans un domaine [0,Lx]x[0,Ly]
    #Les individus se reproduisent au taux taux_de_reproduction :
    #    Le nouvel individu y est situé à une distance r de son parent, où r 
    #    est distribuée selon une loi gamma(a,b). L'angle entre y et sa mere 
    #    sera tiré uniformement entre 0 et 2pi. 
    #Les individus meurent naturellement au taux taux_de_mort_naturelle
    #Les individus meurent à cause de leurs voisins aux taux 
    #taux_de_mort_par_competition*nb de voisins, où un voisin est un individu 
    #situé à une distance inférieure à rayon_du_noyau_de_competition.
    #On fixe également les tailles initiales et maximale de la population ainsi 
    #que le temps maximal de la simulation.
    
    def __init__(self):  
        self.Lx = 100
        self.Ly = 100
        self.taille_initiale_de_la_population = 100
        self.taille_maximale_de_la_population = 1000
        self.taux_de_reproduction = 0.1
        self.taux_de_mort_naturelle = 0.02
        self.taux_de_mort_par_competition = 0.05
        self.rayon_du_noyau_de_competition = 5.
        self.temps_max = 20
        self.noyau_reproduction = (3,4)   #paramètres (a,b) de la loi gamma