from ma_rue import rue, affiche
def couleur_aleatoire():
    '''
    Renvoie une couleur HTML valide
    au format 'rgb(rouge, vert, bleu)'
    où rouge, vert et bleu sont des entiers
    compris entre 0 et 255 choisis aléatoirement.
    
    '''
    from random import randint
    rouge = randint(0,255)
    vert = randint(0,255)
    bleu = randint(0,255)
    return f"rgb({rouge},{vert},{bleu})"
