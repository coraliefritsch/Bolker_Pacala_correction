# -*- coding:Utf-8 -*-
import numpy as np
import random

class individu(object):
    '''un individu est caracterisé par ses coordonnées x et y dans le plan 
        et le nombre de ses voisins'''
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.nbvoisins = 0
        
    def __str__(self):
        '''génère l’affichage (pour la fonction print) d’un individu :
            L'affichage est de type ((x,y),nbvoisins)'''
        return ("((" + str(self.x) + "," + str(self.y) + ")," 
                + str(self.nbvoisins) + ")")
    
    def distance(self,ind, param):
        '''retourne la distance dans le tore [0,Lx]x[0,Ly] entre deux individus 
            (self et ind), où Lx et Ly sont des arguments de param (de la 
            classe paramètres)
        '''
        #La distance dans le tore est au plus la longeur de la demi-diagonale 
        #sqrt((Lx/2)^2+(Ly/2)^2).
        #Si la différence entre les coordonnées en x (resp y) est supérieur à
        # Lx/2 (resp Ly/2), on fait subir une translation suivant l'axe des x 
        #(resp des y) à un des 2 individus pour calculer la distance
        dx = abs(self.x - ind.x)
        dy = abs(self.y - ind.y)
        if dx > param.Lx/2.:
            dx = param.Lx - dx
        if dy > param.Ly/2.:
            dy = param.Ly - dy
        return np.sqrt(dx**2+dy**2)
    
    def nombre_de_voisins(self,popu,param):
        '''retourne le nombre de voisins de l’individu parmi les individus de 
            la population popu:
                un voisin de self est un individu situé à une distance (dans le 
                tore!) inférieure à param.rayon_du_noyau_de_competition
        '''
        #deux individus sont voisins si la distance (dans le tore) qui les 
        #sépare est inférieure à un rayon donné. 
        #le vecteur "voisins" ci-dessous est un vecteur booléen : 
        #    1 si l'individu est un voisin, 0 sinon
        #La somme des éléments de ce vecteur-1 nous donne donc le nombre de 
        #voisins (on soustrait 1 pour ne pas considérer un individu comme étant 
        #son propre voisin)
        voisins = [self.distance(ind,param)<=param.rayon_du_noyau_de_competition 
                 for ind in popu.individus[:popu.taille]]
        return np.sum(voisins) - 1
    
    def naissance(self,param):
        '''crée et retourne le nouvel individu (né de parent self)
            Le nouvel individu est placé à une distance r distribuée par une 
            loi gamma l'angle theta entre le nouvel individu et son parent est 
            distribué uniformément entre 0 et 2pi
            Le nombre de voisin ne sera pas calculé ici
        '''
        r = random.gammavariate(param.noyau_reproduction[0],
                              param.noyau_reproduction[1])
        theta = 2 * np.pi * random.random()
        #on revient ensuite aux coordonnées cartésiennes :
        x = self.x + r * np.cos(theta)
        y = self.y + r * np.sin(theta)
        #Si l'individu sort du domaine on lui fait subir une translation :
        x = x - param.Lx * np.floor(x/param.Lx)
        y = y - param.Ly * np.floor(y/param.Ly)
        return individu(x,y)
    
    
    
