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
    
    rue.fill_style = "YellowGreen" 
    rue.fill_rect(0, 50, 140, 60)
    
    rue.fill_style = "plum" 
    rue.fill_rect(500, 300, 140, 60)
    
    rue.fill_style = "SkyBlue" 
    rue.fill_rect(200, 150, 200, 100)
    
    rue.fill_style = "salmon" 
    rue.fill_rect(250, 200, 100, 50)
    