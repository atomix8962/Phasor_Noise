"""
Nom :           root/interactive.py
Decription :    Script de génération de bruits Phasor avec des paramètres choisis et positionnement des noyaux graphiques
Date :          30/01/2023
Auteur :        Paul B.
Statut :        En rédaction...
"""
"""
A faire: 
- paramètres modulables
- suppression d'un noyau
- visualisation des noyaux (quand selectionné, afficher le vecteur)
"""

# Section des imports
# Os sert a effacer le terminal 
import os
# Matplotlib sert afficher graphiquement le bruit
from matplotlib import pyplot as plt
# Numpy sert à simplifier les calculs matricielles
import numpy as np
# Phasor.phasor_py permet de calculer le bruit phasor avec python
from phasor.phasor_py import apply_noise_py
# Rsc.const permet d'avoir accès aux constantes du projet
from rsc.const import *

# Section de définition des fonctions
"""
onclick prend en argument les données de l'événement qui l'a déclenchée. On récupère les coordonnées 
de la souris puis on recalcule le bruit Phasor avec le nouveau noyau aux coordonnées de la souris
"""
def onclick(event) -> None:
    global kernels
    os.system("cls|clear") # On efface le terminal
    # On affiche la barre de progression et des messages
    print(bcolors.OKGREEN + "Processing ..." + bcolors.ENDC) 
    print()
    kernels.append([[event.xdata, event.ydata], [1,-1], 1, 0.1]) # Définition du nouveau noyau
    img = plt.contourf(X, Y, np.array(apply_noise_py(X, Y, kernels)), cmap="Greys") # Recalcule de l'image du bruit
    print()
    print(bcolors.OKGREEN + "Done !" + bcolors.ENDC)
    fig.canvas.draw_idle() 

# Section du script
os.system("cls|clear") # On efface le terminal
# On affiche la barre de progression et des messages
print(bcolors.OKGREEN + "Processing ..." + bcolors.ENDC) 
print()
size = 100 # Taille de l'image
kernels = list() # Liste des noyaux de bruit phasor

X, Y = np.meshgrid(np.arange(0, size, 1), np.arange(0, size, 1)) # Matrice de base pour l'image
fig = plt.figure("Interactive Phasor Noise Generator") # Nom de la fenêtre
img = plt.contourf(X, Y, np.array(apply_noise_py(X, Y, kernels)), cmap="Greys") # Calcul de base de l'image
plt.colorbar(img) # Gradient de gris en fonction de la valeur du bruit
cid = fig.canvas.mpl_connect('button_press_event', onclick) # Connexion de la fonction onclick à l'évènement 'appuie du bouton souris'

print()
print(bcolors.OKGREEN + "Done !" + bcolors.ENDC)

plt.show() # Affichage

