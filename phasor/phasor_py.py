"""
Nom :           phasor/phasor_py.py
Decription :    Script d'application de bruit Phasor en utilisant uniquement python
Date :          30/01/2023
Auteur :        Alexis
Statut :        Fonctionne en v1.0 (A faire relire par Alexis)
"""

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
def apply_noise_py(X:list, Y:list, kernels:list) -> list:
    Z = list()
    with alive_bar(len(X)*len(Y)) as bar: # Création de la barre de chargement avec la taille de la matrice en nombre de calculs total
        for i in range(len(X)):
            Z.insert(i, [])
            for j in range(len(Y)):
                vector = X[i][j], Y[i][j]
                Z[i].insert(j, generator.phasor_noise(vector, kernels)) # On redéfinit le pixel par la nouvelle valeur calculer avec le bruit Phasor
                bar() # On actualise la barre de chargement
        return Z
  