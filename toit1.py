from ma_rue import rue, affiche 
from random import randint
def toit1( x , niveau):
    '''
    Dessine un triangle plein de couleur noir de 40 pixels de haut
  et avec une base de 160 pixels 
  Paramètres :
      x : abcisse du centre du toit
       niveau : numero du niveau (0 pour les rdc, ...)
    '''
    y = rue.height - niveau * 60 # ordonnée de la base du toit
    rue.line_width = 5

    rue.begin_path()
    rue.move_to(x-70,y)  
    rue.line_to(x,y-40)
    rue.line_to(x+70, y)
    rue.close_path()
    rue.stroke()
    rue.fill_style = "black"
    rue.fill()
    
if __name__ == '__main__':
    affiche(rue)
    toit1(rue.width/2, 0)
    for i in range(5) :
        for j in range(1, 6) :
            toit1(0 + 200 * i, j)