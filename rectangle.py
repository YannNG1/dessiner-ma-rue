# Dépendances
from ma_rue import rue, affiche 

# Définitions

# Fonction rectangle()
def rectangle(x,y,w,h,c):
    '''
    Dessine un rectangle avec un contour noir et rempli de la couleur passée en paramètre
    Paramètres
        x, y : coordonnées du centre de la base de rectangle
        w : largeur du rectangle
        h : hauteur du rectangle
        c : couleur du remplissage
    '''
    
    
    rue.fill_style = c
    rue.fill_rect(x,y,w,h)