"""
Nom :           rsc/img_reader.py
Decription :    Script pour transformer une image en tableau de valeur de pixels
Date :          30/01/2023
Auteur :        Paul M.
Statut :        Fonctionne en v1.0 (vérifié & relu)
"""

# Section des imports
# PIL sert pour analyser une image
from PIL import Image
# Numpy sert a faciliter l'utilisation de tableau sous python
import numpy as np

# Section de définition des fonctions
"""
getImageData retourne la valeur de chaque pixel d'une image (path)
"""
def getImageData(path:str) -> list:
    image = Image.open(path).convert('RGBA')
    image_numpy = np.array(image)
    image_numpy_R = image_numpy[:,:,0].astype(np.float64)/255
    image_numpy_R_flattened = image_numpy_R.reshape((-1,))
    return image_numpy_R_flattened 
