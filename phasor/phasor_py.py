"""
Nom :           phasor/phasor_py.py
Decription :    Script d'application de bruit Phasor en utilisant uniquement python
Date :          30/01/2023
Auteur :        Alexis
Statut :        Fonctionne en v1.0 (A faire relire par Alexis)
"""
import math

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

class PythonPhasorGenerator(generator.PhasorGenerator):

    def exp(self, x):
        return math.exp(x)

    def sin(self, x):
        return math.sin(x)

    def cos(self, x):
        return math.cos(x)

    def atan2(self, x, y):
        return math.atan2(x, y)

    def dot(self, vector1, vector2):
        return vector1[0]*vector2[0]+vector1[1]*vector2[1]

    def vector_subtraction(self, vector1: list, vector2: list):
        return [vector1[0]-vector2[0], vector1[1]-vector2[1]]

def apply_noise_py(X:list, Y:list, kernels:list) -> list:
    Z = list()
    phasor_generator = PythonPhasorGenerator()
    with alive_bar(len(X)*len(Y)) as bar: # Création de la barre de chargement avec la taille de la matrice en nombre de calculs total
        for i in range(len(X)):
            Z.insert(i, [])
            for j in range(len(Y)):
                vector = X[i][j], Y[i][j]
                Z[i].insert(j, phasor_generator.phasor_noise(vector, kernels)) # On redéfinit le pixel par la nouvelle valeur calculer avec le bruit Phasor
                bar() # On actualise la barre de chargement
        return Z
  