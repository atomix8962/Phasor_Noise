"""
Nom :           rsc/img_reader.py
Decription :    Calcule de la moyenne et de l'écart-type des valeurs des pixels d'une image
Date :          30/01/2023
Auteur :        Paul M.
Statut :        Fonctionne en v1.0 (vérifié & relu)
"""
# Section des imports
# PIL sert pour analyser une image
from PIL import Image
# Numpy sert a faciliter l'utilisation de tableau sous python
import numpy as np
# Rsc.img_reader permet de transformer une image en tableau de valeur de pixels
from rsc.img_reader import *

# Section de définition des fonctions
"""
mean permet de calculer la moyenne des pixels passés en arguments
"""
def mean(noiseArray:list)-> float:
    return np.average(noiseArray)

"""
std_gap permet de calculer l'écart-type des pixels passés en arguments
"""
def std_gap(noiseArray:list) -> float:
    return np.std(noiseArray)

"""
test est une fonction de test pour l'image contenu dans rsc/Noise.png
"""
def test():
    data = getImageData("./rsc/Noise.png")
    print(mean(data))
    print(std_gap(data))
    print()