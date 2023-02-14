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

class NumpyPhasorGenerator(generator.PhasorGenerator):

    def exp(self, x):
        return np.exp(x)

    def sin(self, x):
        return np.sin(x)

    def cos(self, x):
        return np.cos(x)

    def atan2(self, x, y):
        return np.arctan2(x, y)

    def dot(self, vector1, vector2):
        return vector1[0]*vector2[0]+vector1[1]*vector2[1]

    def vector_subtraction(self, vector1: list, vector2: list):
        return vector1-vector2
@generator.timeperf
def apply_noise_numpy(X:list, Y:list, kernels:list) -> list:
    Z = NumpyPhasorGenerator().phasor_noise(np.array([X, Y]), kernels)
    return Z

def create_numpy_kernel(kernels, sizeX, sizeY):
    for i in range(len(kernels)):
        kernels[i][0] = np.array([np.full((sizeX, sizeY), kernels[i][0][0]),
                               np.full((sizeX, sizeY), kernels[i][0][1])])
        kernels[i][1] = np.array([np.full((sizeX, sizeY), kernels[i][1][0]),
                               np.full((sizeX, sizeY), kernels[i][1][1])])
    return kernels


X = np.arange(0, 255)
Y = np.arange(0, 255)
X, Y = np.meshgrid(X, Y)
kernel = [[[150, 150], [1, 0], 100, 0.03], [[140, 140], [0, 1], 98, 0.03]]
kernel = create_numpy_kernel(kernel, 255, 255)
print(kernel)
results = apply_noise_numpy(X, Y, kernel)
print(f"Time: {results[1]}")
from matplotlib import pyplot
pyplot.contourf(X, Y, results[0], cmap='Greys')
pyplot.show()
