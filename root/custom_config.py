"""
Nom :           root/custom_config.py
Decription :    Script de génération de bruits Phasor avec des paramètres spécifiques 
Date :          30/01/2023
Auteur :        Paul B.
Statut :        Fonctionne en v1.0 (vérifié & relu)
"""

# Section des imports
# Numpy sert a faciliter l'utilisation de tableau sous python
import numpy as np
# Os sert a effacer le terminal 
import os
# Random permet de générer des valeurs aléatoires sur un intervalle donné par l'utilisateur
import random as rd
# Rsc.const permet d'avoir accès aux constantes du projet
from rsc.const import *
# Phasor.phasor_py permet de calculer le bruit phasor avec python
from phasor.phasor_py import apply_noise_py
# Matplotlib permet d'afficher le bruit généré
from matplotlib import pyplot as plt

# Section de définition des fonction
"""
custom_kernel permet d'afficher l'image générée avec du bruit phasor en fonction d'une taille d'image (size) et d'une liste de noyaux (kernels)
L'image sera de taille : size(en px) * size (en px)
Un noyau est défini par : [position, direction, frequence, largeur]
"""
def custom_kernel(size:int, kernels):
    plt.figure("Custom Phasor Noise") # Nom de la fenêtre
    X, Y = np.meshgrid(np.arange(0, size, 1), np.arange(0, size, 1)) # Création de la matrice de l'image
    img = plt.contourf(X, Y, np.array(apply_noise_py(X, Y, kernels)), cmap="Greys") # Application du bruit sur la matrice 
    plt.colorbar(img) # Gradient de gris en fonction dela valeur du pixel
    plt.show() # Affichage
  
"""
setting est un menu qui permet de choisir la taille de l'image a générer, le nombre de noyaux, 
l'intervalle de l'angle du vecteur d'un noyau, l'intervalle de la largeur de la composante gaussienne du noyau
Par défaut, setting est appelé sans paramètre, si il y a une erreur, la fonction setting sera appelée récursivement
avec en paramètre l'erreur à afficher
En sortie, setting génère une liste de la forme:
[taille, [noyaux]]
Avec un noyau définit par : [postion, direction, frequence, largeur] 
"""
def setting(error:str=None) -> list:
    os.system("cls|clear") # On efface le terminal
    try:
        for f in head: # Affichage du bandeau
            print(f)
        if error != None: # Affichage de l'erreur si elle est définie
            print(error) 

        # Entrées des données des kernels
        size = int(input("Size of the picture: "))
        nb_ker = int(input("Number of kernels: "))
        minFreq = float(input("Minimum of frequency: "))
        maxFreq = float(input("Maximum of frequency: "))
        minAng = float(input("Minum angle of the vector: "))
        maxAng = float(input("Maximum angle of the vector: "))
        minBandwidth= float(input("Gaussian minimum bandwidth: "))
        maxBandwidth= float(input("Gaussian maximum bandwidth: "))

        # Si la frequence et la largeur est fixe pour tous les noyaux
        if minFreq == maxFreq and minBandwidth == maxBandwidth:
            return [size, [[[rd.randint(0,size),rd.randint(0,size)], [np.cos(rd.uniform(minAng,maxAng)),np.sin(rd.uniform(minAng,maxAng))], minFreq, minBandwidth] for i in range(nb_ker)]]
        # Si la frequence est fixe pour tous les noyaux
        elif minFreq == maxFreq:
            return [size, [[[rd.randint(0,size),rd.randint(0,size)], [np.cos(rd.uniform(minAng,maxAng)),np.sin(rd.uniform(minAng,maxAng))], minFreq, rd.uniform(minBandwidth,maxBandwidth)] for i in range(nb_ker)]]
        # Si la largeur est fixe pour tous les noyaux
        elif minBandwidth == maxBandwidth:
            return [size, [[[rd.randint(0,size),rd.randint(0,size)], [np.cos(rd.uniform(minAng,maxAng)),np.sin(rd.uniform(minAng,maxAng))], rd.uniform(minFreq, maxFreq), minBandwidth] for i in range(nb_ker)]]
        # Si tous les paramètres sont aléatoirements choisis dans un intervalle définit
        else:
            return [size, [[[rd.randint(0,size),rd.randint(0,size)], [np.cos(rd.uniform(minAng,maxAng)),np.sin(rd.uniform(minAng,maxAng))], rd.uniform(minFreq, maxFreq), rd.uniform(minBandwidth,maxBandwidth)] for i in range(nb_ker)]]
    
    except:
        return setting(bcolors.FAIL +"An error occured..." + bcolors.ENDC) # Si une erreur quelconque a été détectée


# Section du script
sett = setting() # On récupère les données de génération du bruit Phasor
os.system("cls|clear") # On efface le terminal
# On affiche la barre de progression et des messages
print(bcolors.OKGREEN + "Processing ..." + bcolors.ENDC) 
print()
custom_kernel(sett[0], sett[1]) # On affiche l'image générée
print()
print(bcolors.OKGREEN + "Done !" + bcolors.ENDC)
        
