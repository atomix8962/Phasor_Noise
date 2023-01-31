"""
Nom :           root/gaussian_repr.py
Decription :    Affichage de la gaussienne du calcul du bruit Phasor (script de compréhension)
Date :          30/01/2023
Auteur :        Alexis 
Statut :        Fonctionne en v1.0 (vérifié & relu)
"""

# Section des imports
# Os sert a effacer le terminal 
import os
# Rsc.const permet d'avoir accès aux constantes du projet
from rsc.const import *
# Matplotlib sert afficher graphiquement la gaussienne 
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider
# Numpy sert à simplifier les calculs matricielles (utilisé ici pour allèger l'écriture ) 
import numpy as np
# Phasor.phasor_gen permet de calculer le bruit phasor en un seul point 
import phasor.phasor_gen as generator
#Alive_progress permet d'afficher une barre de chargement durant les calculs et permet d'estimer le temps restants de calculs
from alive_progress import alive_bar

# Section de définition des fonctions
"""
apply_function prend en paramètre une matrice et une largeur (bandwidth) et 
retourne une matrice avec la valeur de la gaussienne
"""
def apply_function(X:list, Y:list, bandwidth:float) -> list:
    Z = []
    with alive_bar(len(X)*len(Y)) as bar: # Création de la barre de chargement avec la taille de la matrice en nombre de calculs total
        for i in range(len(X)):
            Z.insert(i, [])
            for j in range(len(Y)):
                vector = X[i][j], Y[i][j]
                Z[i].insert(j, generator.gaussian(vector, bandwidth)) # Calcul de la valeur de la gaussienne
                bar() # On actualise la barre de chargement
    return Z

"""
update prend en paramètre la valeur de largeur du slider (val) et modifie l'affichage graphique 
pour afficher la nouvelle gaussienne 
"""
def update(val):
    global line
    os.system("cls|clear") # On efface le terminal
    # On affiche la barre de progression et des messages
    print(bcolors.OKGREEN + "Processing ..." + bcolors.ENDC) 
    print()
    line.remove() # On supprime l'ancienne gaussienne
    line = ax.plot_surface(X, Y, np.array(apply_function(X, Y, val)), color="blue") # Calcul et affichage de la nouvelle gaussienne
    print()
    print(bcolors.OKGREEN + "Done !" + bcolors.ENDC)

# Section du script
os.system("cls|clear") # On efface le terminal
# On affiche la barre de progression et des messages
print(bcolors.OKGREEN + "Processing ..." + bcolors.ENDC) 
print()
X, Y = np.meshgrid(np.arange(-10, 10, 0.1), np.arange(-10, 10, 0.1)) # Création de la matrice de base
# Paramétrage de pyplot 
fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))
fig.subplots_adjust(bottom=0.25)
fig.canvas.set_window_title("Gaussian Representation")
line = ax.plot_surface(X, Y, np.array(apply_function(X, Y, 0))) # Calcul de la gaussienne

# Paramétrage du slider
sliderAxes = fig.add_axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(ax=sliderAxes, label='Bandwidth', valmin=0, valmax=3, valinit=0)

slider.on_changed(update) # Si on modifie le slider

print()
print(bcolors.OKGREEN + "Done !" + bcolors.ENDC)
plt.show() # Affichage graphique



