"""
Nom :           phasor/phasor_numpy.py
Decription :    Script de calcul en un point du bruit Phasor avec la bibliothèque NUMPY
Date :          30/01/2023
Auteur :        Paul B.
Statut :        En rédaction...
"""

# Section des imports
# Numpy sert a faciliter l'utilisation de tableau sous python
import numpy as np
# Section des imports
#Alive_progress permet d'afficher une barre de chargement durant les calculs et permet d'estimer le temps restants de calculs
from alive_progress import alive_bar
# Phasor.phasor_py permet de calculer le bruit phasor avec python
import phasor.phasor_gen as generator       

# Section de définition des fonctions
"""
apply_function applique à une matrice la fonction de bruit Phasor avec les noyaux passés en arguments
Matrice : X, Y -> np.meshgrid()
Un noyau est défini par : [position, direction, frequence, largeur]
"""
def apply_noise_numpy(X:list, Y:list, kernels:list) -> list:
    size = 250
    vectors = []
    for x in range(size):
        lx = []
        for y in range(size):
            lx.append([x,y])
        vectors.append(lx)
    Z = np.array(vectors)
    vect_gen = np.vectorize(generator.phasor_noise)
    vect_gen.excluded.add(1)
    Z = vect_gen(Z, kernels) # On redéfinit le pixel par la nouvelle valeur calculer avec le bruit Phasor
    return Z