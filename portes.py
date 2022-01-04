# Dépendances
from ma_rue import rue, affiche
from rectangle import rectangle
from couleur_aleatoire import couleur_aleatoire
from math import pi
from random import randint

# Définitions

# Fonction portes()
def portes(x,y):
    '''
    Dessine une porte de 50 pixels en largeur et 70 pixels en hauteur
    La forme du haut de la porte est aléatoirement rectangulaire ou arrondi
    La couleur pleine de remplissage est choisi aléatoirement parmi les couleurs HTML valides
    Paramètres :
        x est l'abcisse du milieu de la base de la porte
        y est l'ordonnée du sol du niveau de la porte        
    '''        
    
    a=randint(1,2)

    if a == 1:
        rectangle(x-25,y,50,70,couleur_aleatoire())
        rue.rect_cap = "square"
    else:
        rectangle(x-25,y,50,70,couleur_aleatoire()) 
        rue.rect_cap = "round"
    
    
if __name__ == '__main__': 

# Tests
	affiche(rue)
	for i in range(21) :
    	portes(0 + i * 60,rue.height)