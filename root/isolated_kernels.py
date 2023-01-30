"""
Nom :           root/isolated_kernels.py
Decription :    Script de génération de bruits Phasor avec des paramètres choisis et 4 noyaux qui ne se méléange pas avec affichage graphique des paramètres
Date :          30/01/2023
Auteur :        Paul B.
Statut :        Fonctionne en v1.0 (vérifié & relu)
"""

# Section des imports
# Os sert a effacer le terminal 
import os
# Matplotlib sert afficher graphiquement le bruit
from matplotlib import pyplot as plt
# Numpy sert à simplifier les calculs matricielles
import numpy as np
# Phasor.phasor_py permet de calculer le bruit phasor avec python
import phasor.phasor_py as generator
# Rsc.const permet d'avoir accès aux constantes du projet
from rsc.const import *
#Alive_progress permet d'afficher une barre de chargement durant les calculs et permet d'estimer le temps restants de calculs
from alive_progress import alive_bar

# Section de définition des fonctions
"""
apply_function applique à une matrice la fonction de bruit Phasor avec les noyaux passés en arguments
Matrice : X, Y -> np.meshgrid()
Un noyau est défini par : [position, direction, frequence, largeur]
"""
def apply_function(X:list, Y:list, kernels:list) -> list:
    Z = []
    with alive_bar(len(X)*len(Y)) as bar: # Création de la barre de chargement avec la taille de la matrice en nombre de calculs total
        for i in range(len(X)):
            Z.insert(i, [])
            for j in range(len(Y)):
                vector = X[i][j], Y[i][j]
                Z[i].insert(j, generator.phasor_noise(vector, kernels)) # # On redéfinit le pixel par la nouvelle valeur calculer avec le bruit Phasor
                bar() # On actualise la barre de chargement
    return Z

# Section du script
os.system("cls|clear") # On efface le terminal
# On affiche la barre de progression et des messages
print(bcolors.OKGREEN + "Processing ..." + bcolors.ENDC) 
print()

plt.figure('4 kernels isolated') # Nome de la fenêtre
kernels = [[[25, 25], [1, 1], .75, 0.1], [[25, 75], [1, 0], .75, 0.1], [[75, 25], [0, 1], .75, 0.1], [[75, 75], [-1, 1], .75, 0.1]] # Noyaux pré-définient

X, Y = np.meshgrid(np.arange(0, 100, 1), np.arange(0, 100, 1)) # Matrice de base de l'image en 100*100

img = plt.contourf(X, Y, np.array(apply_function(X, Y, kernels)), cmap="Greys") # Calcul du bruit phasor de l'image
plt.colorbar(img) # Gradient de gris en fonction de la valeur du bruit

# Affichage des vecteurs et des noyaux
for kernel in kernels:
    plt.plot(kernel[0][0],kernel[0][1], color="green", marker="o")
    plt.arrow(kernel[0][0],kernel[0][1], kernel[1][0]*15,kernel[1][1]*15 , width= 1,head_width=4, head_length=4, color="red")

print()
print(bcolors.OKGREEN + "Done !" + bcolors.ENDC)

plt.show() # Affichage
